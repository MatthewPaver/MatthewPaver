import hashlib
import os
from pinscrape import pinscrape

def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def remove_duplicates(directory):
    downloaded_hashes = set()
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_hash = hash_file(filepath)
            if file_hash in downloaded_hashes:
                os.remove(filepath)
                print(f"Duplicate removed: {filename}")
            else:
                downloaded_hashes.add(file_hash)

def download_images(search_term, output_directory, proxy_list, num_threads, max_images):
    details = pinscrape.scraper.scrape(search_term, output_directory, proxy_list, num_threads, max_images)

    if details["isDownloaded"]:
        print(f"\nDownloading for '{search_term}' completed !!")
        print(f"\nTotal urls found for '{search_term}': {len(details['extracted_urls'])}")
        print(f"\nTotal images downloaded for '{search_term}': {len(details['url_list'])}")
        remove_duplicates(output_directory)
    else:
        print(f"\nNothing to download for '{search_term}' !!")

def is_deepest_folder(directory):
    # A folder is deepest if it contains no subdirectories
    return not any(os.path.isdir(os.path.join(directory, sub)) for sub in os.listdir(directory) if not sub.startswith('.'))

def get_deepest_folders(base_directory):
    deepest_folders = []
    for root, dirs, files in os.walk(base_directory):
        if is_deepest_folder(root):
            deepest_folders.append(root)
    return deepest_folders

# Base directory where the folders are located
base_directory = "/Users/mattpaver/Desktop/Images"

# Get the deepest folders
deepest_folders = get_deepest_folders(base_directory)

# Loop through the deepest folders and download images using the folder name as the search term
for folder in deepest_folders:
    search_term = os.path.basename(folder)
    download_images(search_term, folder, {}, 10, 1000)
