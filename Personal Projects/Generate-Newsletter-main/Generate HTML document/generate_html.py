
import os
import pandas as pd
from datetime import datetime

class HTML_Generation:
    def __init__(self):
        # data directories
        self.dirname = os.path.dirname
        self.join = os.path.join
        data_dir = self.join(self.dirname(__file__), 'data')
        templates_dir = self.join(self.dirname(__file__), 'templates')
        newsletter_dir = self.join(self.dirname(__file__), 'newsletters')
        
        self.data_dir = os.path.normpath(data_dir)
        self.templates_dir = os.path.normpath(templates_dir)
        self.newsletter_dir = os.path.normpath(newsletter_dir)
        
        # date
        today = datetime.now()
        self.month_index = today.strftime("%m")
        self.month = today.strftime("%B")
        self.year_index = today.strftime("%y")
        self.year = today.strftime("%Y")
        self.filename = str(self.month_index + "-" + self.year_index)
        
        # Load templates
        with open(self.join(self.templates_dir, 'header_template.html'), 'r') as file:
            self.header_template = file.read()
        with open(self.join(self.templates_dir, 'section_header_template.html'), 'r') as file:
            self.section_header_template = file.read()
        with open(self.join(self.templates_dir, 'sub_section_header_template.html'), 'r') as file:
            self.sub_section_header_template = file.read()
        with open(self.join(self.templates_dir, 'article_img_template.html'), 'r') as file:
            self.article_img_template = file.read()
        with open(self.join(self.templates_dir, 'footer_template_web.html'), 'r') as file:
            self.footer_template = file.read()

    def load_articles_data(self):
        # Load cleaned_articles.csv
        self.articles_df = pd.read_csv(self.join(self.data_dir, 'cleaned_articles.csv'))
        # Remove trailing whitespace from the "Category" column
        self.articles_df['Category'] = self.articles_df['Category'].str.strip()
    
    def generate_html(self):
        # Integrate header
        self.html = self.header_template.replace("MONTH YEAR", self.month + " " + self.year)
        
        # Integrate Project Delivery section header
        self.html += self.section_header_template.replace("Section", "Project Delivery")
        
        # Integrate articles by category
        categories = ["Construction", "Energy", "Transport", "Project Management", "Other", "AI & Machine Learning", "Data Analytics"]
        
        # Integrate Data subsection header before AI & Machine Learning
        data_subsection_position = categories.index("AI & Machine Learning")
        categories.insert(data_subsection_position, "Data")
        
        for category in categories:
            # Skip the Data category as it's just a subsection header without articles
            if category == "Data":
                self.html += self.section_header_template.replace("Section", "Data")
                continue
            
            # Integrate subsection header
            self.html += self.sub_section_header_template.replace("Sub Section", category)
            
            # Integrate articles for this category
            category_articles = self.articles_df[self.articles_df['Category'] == category]
            for _, row in category_articles.iterrows():
                article_content = self.article_img_template
                article_content = article_content.replace("img_link", row['Image URL'])
                article_content = article_content.replace("url", row['Article URL'])
                article_content = article_content.replace("Title", row['Article'])
                formatted_date = pd.to_datetime(row['Published Date']).strftime('%d/%m/%y')
                author_info = f"{formatted_date} - By {row['Author']} - {row['Website']}"
                article_content = article_content.replace("Date - By Author", author_info)
                article_content = article_content.replace("Body", row['Summary'])
                self.html += article_content
        
        # Integrate footer
        self.html += self.footer_template
        
        # Save html without overwriting existing files
        original_name = f"{self.filename}_web.html"
        save_path = self.join(self.newsletter_dir, original_name)
        counter = 1
        name, extension = os.path.splitext(original_name)
        while os.path.exists(save_path):
            new_name = f"{name}_{counter}{extension}"
            save_path = self.join(self.newsletter_dir, new_name)
            counter += 1

        with open(save_path, "w", encoding='utf-8') as file:
            file.write(self.html)

        final_file = os.path.basename(save_path)
        print('Newsletter Generation script has finished running.')
        print(f'The html file can be found at: newsletters/{final_file}')

if __name__ == "__main__":
    HTML = HTML_Generation()
    HTML.load_articles_data()
    HTML.generate_html()
