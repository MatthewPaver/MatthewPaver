"""Browser QA for the ProjectLens and DecisionGraph portfolio entries."""

from playwright.sync_api import sync_playwright


BASE_URL = "http://127.0.0.1:8878/store/"


def assert_no_overflow(page):
    assert page.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    errors = []
    page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    assert_no_overflow(page)

    card = page.locator('[data-slug="projectlens"]')
    assert card.count() == 1
    assert "Checks whether a project change is ready to decide" == card.get_attribute("data-solves")
    assert card.locator('img[src*="projectlens-change-assurance.png"]').count() == 1
    assert card.locator('a[href="https://matthewpaver.github.io/ProjectLens/change-assurance.html"]').count() == 1

    page.goto(f"{BASE_URL}preview.html?app=projectlens")
    page.wait_for_load_state("networkidle")
    assert "decision blockers" in page.locator("#preview-summary").inner_text().lower()
    assert page.locator('a[href="https://matthewpaver.github.io/ProjectLens/change-assurance.html"]').count() == 1

    mobile = browser.new_page(viewport={"width": 390, "height": 844})
    mobile.goto(BASE_URL)
    mobile.wait_for_load_state("networkidle")
    assert_no_overflow(mobile)
    assert mobile.locator('[data-slug="projectlens"]').is_visible()
    assert not errors, errors
    browser.close()

print("Portfolio browser QA passed: ProjectLens card, preview, links and mobile")
