
import csv
import re
import os
import pandas as pd
from gnews import GNews
from datetime import datetime
from transformers import T5Tokenizer, T5ForConditionalGeneration
import language_tool_python

# Define the filename based on the script directory
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_directory, 'scraped_articles.csv')
searchquery = os.path.join(script_directory, 'search querys.txt')

# Read categories and search queries from the text file
categories = {}
with open(searchquery, 'r') as file:
    lines = file.readlines()
    for line_number, line in enumerate(lines, start=1):
        # Skip blank or whitespace-only lines
        if not line.strip():
            continue
        
        cleaned_data = line.replace("{", "").replace("}", "").strip().split(":")
        try:
            category = cleaned_data[0].strip(" '")
            queries = [query.strip(" '") for query in cleaned_data[1].strip(" []").split(",")]
            categories[category] = queries
        except IndexError:
            print(f"Error processing line {line_number}: {line}")
            continue


# Initialize GNews
google_news = GNews()

# Initialize the LanguageTool object for grammar and spelling correction
tool = language_tool_python.LanguageTool('en-US')

# Function to correct grammar and spelling
def correct_text(text):
    matches = tool.check(text)
    offset_correction = 0
    for match in matches:
        offset = match.offset + offset_correction
        length = match.errorLength
        replacement = match.replacements[0] if match.replacements else ""
        text = text[:offset] + replacement + text[offset + length:]
        offset_correction += len(replacement) - length
    return text

# Summarize function
def summarize(text):
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    tokenizer = T5Tokenizer.from_pretrained("t5-small", use_legacy_mode=False)
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=10, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

data_rows = []

for category, searches in categories.items():
    for query in searches:
        current_month = datetime.now().strftime('%Y-%m')
        news_results = google_news.get_news(query + ' date:' + current_month)
        if not news_results:
            print(f"No articles found for query: {query}")
            continue
        news_results = news_results[:3]
        for article in news_results:
            raw_url = article['url']  # Directly use the raw URL
            full_article = google_news.get_full_article(raw_url)
            if full_article:
                authors = ', '.join(full_article.authors)
                description = correct_text(full_article.text)
            else:
                authors = ''
                description = ''

            summary_text = summarize(description)
            summary_text = correct_text(summary_text)

            data_row = {
                'Category': category,
                'Website': article['publisher']['title'] if 'title' in article['publisher'] else '',
                'Article': article['title'].split(' - ')[0] if ' - ' in article['title'] else article['title'],
                'Author': authors,
                'Article URL': raw_url,
                'Description': description,
                'Summary': summary_text,
                'Published Date': datetime.strptime(article['published date'], '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%y'),
                'Scraped Date': datetime.now().strftime('%d/%m/%y'),
                'Image URL': '',
                'Approve article': ''
            }
            data_rows.append(data_row)

# Convert list of dicts to DataFrame
df = pd.DataFrame(data_rows)

# Clean URLs
def clean_url(url):
    unwanted_prefix = 'https://consent.google.com/m?continue='
    if url.startswith(unwanted_prefix):
        return url[len(unwanted_prefix):]
    return url

df['Article URL'] = df['Article URL'].apply(clean_url)

# Remove duplicates based on 'Article URL'
df = df.drop_duplicates(subset='Article URL')

# Write DataFrame to CSV
df.to_csv(filename, index=False, mode='a')

print(f"Data written to {filename}")
