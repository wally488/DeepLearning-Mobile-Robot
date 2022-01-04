

import sys

from fastai.vision import *
from google.colab import drive, files
from google_images_download import google_images_download
from selenium import webdriver  # needed for google_images_download

# Put chromedriver in the right spot
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

# set options to be headless, ..
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# mount google drive
drive.mount('/content/drive')

output_directory = "/content/drive/My Drive/anime_vs_cartoon_images"

# Category Google Searches
# `-` excludes the string from the search
categories = {"bike": "bike",
              "bicycle": "bicycle"}
              
def download_images(query, **kwargs):
    """
    Args:
        query (str): The search string to use with Google Images.
        **kwargs: See https://github.com/hardikvasa/google-images-download/blob/master/google_images_download/google_images_download.py#L65 for options.
    Returns
        List of paths to download files.
    """
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": query,
                 "limit": 75,
                 "print_urls": False,
                 "chromedriver": "/usr/bin/chromedriver"}
    arguments.update(kwargs)
    paths = response.download(arguments)
    
    return paths[0][query]

img_paths = {}
for name, query in categories.items():
    img_paths[name] = download_images(query=query,
                                      output_directory=output_directory,
                                      image_directory=name)
