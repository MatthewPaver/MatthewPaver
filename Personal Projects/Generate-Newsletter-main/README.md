# Generate-Newsletter

## Description:
The "Newsletter from Scratch" project is a comprehensive automation system designed to simplify the process of curating news articles from various sources and presenting them in a visually appealing HTML-based newsletter. By utilizing modern web scraping techniques and advanced data transformation methods, this system ensures that the end-users are always updated with the most relevant and recent news articles in their areas of interest.

## How It Works:
**Article Collection:**

The main.py script in the "Collect News Articles" directory uses predefined search queries from search querys.txt to scrape relevant news articles.
Leveraging the power of the gnews library, it fetches articles from various reputable sources, ensuring diversity and credibility in the news presented.
The details of the scraped articles, such as title, author, URL, and summary, are then stored in the scraped_articles.csv file for further processing.
Newsletter Generation:

The generate_html.py script in the "Generate HTML document" directory takes the collected articles from scraped_articles.csv.
Using predefined templates from the "templates" directory, it crafts an HTML document that presents the articles in a structured and visually appealing manner.
Images related to the articles, if present, are fetched from the "images" directory, enhancing the visual presentation.
The final newsletter is saved in the "newsletters" directory, ready for distribution.
Directory Structure:

- Collect News Articles:
  - main.py: The heart of the article scraping process.
  - scraped_articles.csv: A datastore for the scraped articles.
  - search querys.txt: A list of search queries guiding the scraping.
- Generate HTML document:
  - generate_html.py: Transforms the scraped articles into a newsletter.
  - data: Supplementary data for the newsletter generation.
  - images: Visual assets for the newsletter.
  - newsletters: Archive of generated newsletters.
  - templates: HTML templates guiding the newsletter's look and feel.
