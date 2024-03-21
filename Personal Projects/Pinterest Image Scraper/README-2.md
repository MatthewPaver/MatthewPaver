# Pinterest Image Scraper

This Python script is designed to automate the process of scraping and downloading images from Pinterest. It utilizes search terms derived from the names of the deepest subdirectories within a specified base directory, ensuring a topic-specific collection of images. Additionally, the script includes functionality to remove duplicate images based on content hashing, maintaining a unique set of images in each directory.

## Features

- **Automatic Image Downloading**: Downloads images from Pinterest based on directory-derived search terms.
- **Duplicate Removal**: Ensures all downloaded images are unique within their respective directories.
- **Multi-threading Support**: Allows for faster downloads by leveraging multiple threads.
- **Proxy Support**: Capable of using proxy lists to bypass network restrictions or for privacy reasons.

## Prerequisites

- Python 3.x
- `pinscrape` module (This seems to be a custom or third-party module, so make sure to provide installation instructions or a link to its source.)

## Setup

1. Ensure Python 3 is installed on your system.
2. Install the `pinscrape` module. (Include specific installation commands or steps here.)
3. Clone or download this script to your local machine.

## Usage

1. Open the script in a text editor and set the `base_directory` variable to the path of your base directory containing the deepest subdirectories for which you want to download images.
2. Run the script with the following command:
    ```shell
    python "Pinterest image scraper.py"
    ```
3. The script will automatically process each deepest subdirectory, use its name as a search term to download images from Pinterest, and save them in the same subdirectory.

## Important Notes

- Ensure you have the necessary permissions to scrape and download images from Pinterest.
- The efficiency and speed of downloading can vary based on the number of threads and the use of proxies.
- The script removes duplicates post-download, which may slightly extend the overall processing time.

## Disclaimer

This script is provided for educational and research purposes only. Always respect Pinterest's terms of service and ensure you have the right to download and use the images.