from playwright.sync_api import sync_playwright


BASE_URL = "http://127.0.0.1:4180/store/"


def assert_no_horizontal_overflow(page) -> None:
    dimensions = page.evaluate(
        """() => ({
          content: document.documentElement.scrollWidth,
          viewport: window.innerWidth
        })"""
    )
    assert dimensions["content"] <= dimensions["viewport"], dimensions


with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    console_errors: list[str] = []
    page.on(
        "console",
        lambda message: console_errors.append(message.text)
        if message.type == "error"
        else None,
    )

    page.goto(BASE_URL, wait_until="networkidle")
    assert page.locator(".task-route").count() == 3
    assert page.locator(".app-card").count() == 14
    assert page.locator("#visible-count").inner_text() == "14"
    assert page.locator('a[href="https://matthewpaver.github.io/MeetingProof/"]').count() >= 1
    assert page.locator(
        'a[href="https://matthewpaver.github.io/ProjectLens/change-assurance.html"]'
    ).count() >= 1
    assert page.locator('a[href="https://matthewpaver.github.io/DecisionGraph/"]').count() >= 1

    page.locator('button[data-filter="work"]').click()
    visible_slugs = page.locator(".app-card:not(.hidden)").evaluate_all(
        "(cards) => cards.map((card) => card.dataset.slug)"
    )
    assert visible_slugs == ["meetingproof", "projectlens", "decisiongraph"], visible_slugs
    assert "filter=work" in page.url

    page.goto(f"{BASE_URL}preview.html?app=meetingproof", wait_until="networkidle")
    assert page.locator("h1").inner_text() == "MeetingProof"
    assert "human reviewer" in page.locator("body").inner_text().lower()
    page.screenshot(path="/tmp/portfolio-meetingproof-preview.png", full_page=True)
    assert_no_horizontal_overflow(page)

    mobile = browser.new_page(viewport={"width": 390, "height": 844})
    mobile.goto(BASE_URL, wait_until="networkidle")
    assert mobile.locator(".task-route").count() == 3
    assert mobile.locator(".task-route-primary .workbench-preview").is_visible()
    assert_no_horizontal_overflow(mobile)
    mobile.screenshot(path="/tmp/portfolio-task-first-mobile.png", full_page=True)

    page.goto(f"{BASE_URL}workbench.html", wait_until="networkidle")
    assert page.locator("[data-tool-tab]").count() == 3
    assert "stays in this browser" in page.locator("body").inner_text()
    page.locator('[data-sample="update"]').click()
    page.locator("#build-update").click()
    assert page.locator(".result-section").count() == 5
    assert "Supplier shortlist agreed" in page.locator("#workbench-output").inner_text()
    assert "Source line 1" in page.locator("#workbench-output").inner_text()
    assert page.locator("#export-result").is_enabled()

    page.locator('[data-tool-tab="handover"]').click()
    page.locator('[data-sample="handover"]').click()
    page.locator("#build-handover").click()
    assert page.locator(".result-section").count() == 6
    assert "Project Cedar" in page.locator("#workbench-output").inner_text()

    page.locator('[data-tool-tab="change"]').click()
    page.locator('[data-sample="change"]').click()
    page.locator("#compare-change").click()
    assert page.locator(".change-totals").is_visible()
    assert page.locator(".change-added li").count() == 4
    assert page.locator(".change-removed li").count() == 4
    page.screenshot(path="/tmp/everyday-workbench-desktop.png", full_page=True)
    assert_no_horizontal_overflow(page)

    workbench_mobile = browser.new_page(viewport={"width": 390, "height": 844})
    workbench_mobile.goto(f"{BASE_URL}workbench.html", wait_until="networkidle")
    workbench_mobile.locator('[data-tool-tab="change"]').click()
    workbench_mobile.locator('[data-sample="change"]').click()
    workbench_mobile.locator("#compare-change").click()
    assert workbench_mobile.locator(".change-totals").is_visible()
    assert_no_horizontal_overflow(workbench_mobile)
    workbench_mobile.screenshot(path="/tmp/everyday-workbench-mobile.png", full_page=True)

    no_js_context = browser.new_context(java_script_enabled=False)
    no_js = no_js_context.new_page()
    no_js.goto(BASE_URL, wait_until="domcontentloaded")
    assert no_js.locator(".task-route").count() == 3
    assert no_js.locator(".no-script-shelves").is_visible()
    assert no_js.locator(".filters").is_hidden()
    assert no_js.locator('a[href="?filter=work#project-grid-heading"]').is_visible()
    assert no_js.locator('a[href="https://matthewpaver.github.io/MeetingProof/"]').count() >= 1
    no_js_context.close()

    assert not console_errors, console_errors
    browser.close()

print("Task-first portfolio browser QA passed: routes, filter, preview, desktop and mobile.")
