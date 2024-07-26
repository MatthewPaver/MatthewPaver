# Contents

## Generate-Newsletter

### Description

The "Newsletter from Scratch" project automates the process of curating news articles and presenting them in an HTML-based newsletter. Using web scraping and data transformation, it ensures users receive the most relevant and recent news in their areas of interest.

### How It Works

- **Article Collection**: `main.py` in the "Collect News Articles" directory uses `search querys.txt` to scrape articles via the gnews library, storing details in `scraped_articles.csv`.
- **Newsletter Generation**: `generate_html.py` in the "Generate HTML document" directory transforms the articles from `scraped_articles.csv` into an HTML newsletter using templates and images, saving the output in the "newsletters" directory.

### Directory Structure

- **Collect News Articles**:
  - `main.py`
  - `scraped_articles.csv`
  - `search querys.txt`
- **Generate HTML document**:
  - `generate_html.py`
  - `data`
  - `images`
  - `newsletters`
  - `templates`

---

## HR Performance Reporting Dashboards

### Overview

This project provides HR performance reports for a global utility products company. It addresses issues like high absences and poor service delivery, using Excel 2021 for data analysis and Power BI for visualizations.

### Contents

1. **HR Performance Reporting Dashboards.pbix**: Power BI dashboard file.
   ![Performance Report Summary](https://github.com/MatthewPaver/MatthewPaver/blob/main/Personal%20Projects/HR%20Performance%20Reporting%20Dashboards/Dashboard%20Images/HR%20Performance%20Reporting%20Summary.png)
2. **High Sick Leave.csv & Low Sick Leave.csv**: Lists of employees with high and low sick leave.
   ![Performance Report Sick Leave](https://github.com/MatthewPaver/MatthewPaver/blob/main/Personal%20Projects/HR%20Performance%20Reporting%20Dashboards/Dashboard%20Images/HR%20Performance%20Reporting%20Sick%20Leave.png)
3. **TopSalesPerformers.csv**: Top sales performers.
   ![Performance Report Sales](https://github.com/MatthewPaver/MatthewPaver/blob/main/Personal%20Projects/HR%20Performance%20Reporting%20Dashboards/Dashboard%20Images/HR%20Performance%20Reporting%20Sales.png)

### Documentation

- [**HR Performance Reporting Dashboards.pdf**](https://github.com/MatthewPaver/MatthewPaver/blob/main/Personal%20Projects/HR%20Performance%20Reporting%20Dashboards/HR%20Performance%20Reporting%20Dashboards.pdf)
- [**Project A HR Performance Reporting Documentation.pdf**](https://github.com/MatthewPaver/MatthewPaver/blob/main/Personal%20Projects/HR%20Performance%20Reporting%20Dashboards/Project%20A%20HR%20Performance%20Reporting%20Documentation.pdf)

### Key Insights

- 61.72% of employees work in Production.
- Average sick leave per employee is 9.09 hours/year.
- Positive correlation between Sales YTD and Sales Last Year.

### Getting Started

1. **Power BI Dashboards**: Open `.pbix` file in Power BI Desktop.
2. **CSV Datasets**: View with spreadsheet software like Excel.
3. **PDF Documentation**: View with any standard PDF reader.

### Exercises

- Analyze the data using the provided CSV files.
- Enhance the dashboards in Power BI.
- Draft recommendations based on your analysis.

---

## Pinterest Image Scraper

### Description

This Python script automates scraping and downloading images from Pinterest based on search terms derived from subdirectory names. It ensures a unique set of images by removing duplicates based on content hashing.

### Features

- Automatic Image Downloading
- Duplicate Removal
- Multi-threading Support
- Proxy Support

### Prerequisites

- Python 3.x
- `pinscrape` module

### Setup

1. Ensure Python 3 is installed.
2. Install `pinscrape` using `pip install pinscrape`.
3. Clone or download the script.

### Usage

1. Set the `base_directory` variable to the path of your base directory.
2. Run the script:
   ```sh
   python "Pinterest image scraper.py"
      ```

### Important Notes

- Ensure permissions for scraping and downloading images from Pinterest.
- Efficiency varies based on threads and proxies.
- Duplicate removal extends processing time.

### Disclaimer

This script is for educational and research purposes only. Always respect Pinterest's terms of service and ensure you have the rights to use the images.

---

## PySpark and Kafka Integration Example

### Overview
This repository demonstrates the integration of PySpark with Apache Kafka for real-time data streaming and processing. It illustrates how PySpark can consume and process streaming data from Kafka topics, perform basic DataFrame operations, and output the processed data.

### Prerequisites
- Java Development Kit (JDK)
- Apache Spark
- Python with PySpark installed
- Apache Kafka

### How It Works
1. **Start Zookeeper**: Initialize the Zookeeper server required by Kafka.
2. **Start Kafka Server**: Launch the Kafka server to handle messaging.
3. **Create Kafka Topic**: Set up a Kafka topic named `test-topic`.
4. **Execute PySpark Script**: Run the PySpark script to process streaming data from Kafka.

### PySpark Scripts
- **Example 1**: Creates a simple DataFrame and displays its contents.
- **Example 2**: Reads and processes streaming data from a Kafka topic using PySpark, then writes the output to the console.

### Conclusion
This example showcases setting up and running a PySpark application that processes real-time data from Kafka, highlighting the integration between PySpark and Kafka for efficient streaming data processing.



