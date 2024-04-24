# AI Article Scraper

## Description:
This project is designed to scrape news articles based on specific search queries related to various categories like construction, energy, transport, AI & machine learning, and more. The scraped articles are stored in a CSV file with details such as the article's category, title, author, URL, and more.

## Files in the Repository:

**main.py**: The main script responsible for scraping articles based on search queries and storing them in a CSV format.
**scraped_articles.csv**: A CSV file containing the details of the scraped articles.
**search querys.txt**: A file containing categories and their associated search queries.

## How to Run:
Ensure you have all the prerequisites installed (see PREREQUISITES.md).
Run the main.py script.
Check the scraped_articles.csv for the scraped articles.

## Prerequisites:

Before running the main.py script, ensure you have the following prerequisites installed:

**Python 3.x**
Required Python Libraries:
- pandas: _pip install pandas_
- gnews: _pip install gnews_
- transformers: _pip install transformers_
- language_tool_python: _pip install language_tool_python_
(Note: Some libraries like csv, re, os, and datetime are part of Python's standard library and do not need to be installed separately.)
