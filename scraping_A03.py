#### Bella Fishman
#### A03 data mining
#### year in review
from datetime import date
import time
import csv
import os
import requests
import urllib
from bs4 import BeautifulSoup, NavigableString
import re
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import basic_stats, process_articles
import config

session = requests.Session()

# backoff factor is delay between retries
# connect is number of retries in a connection error event
retry = Retry(connect=7, backoff_factor=5)

adapter = HTTPAdapter(max_retries=retry)

session.mount('http://', adapter)
session.mount('https://', adapter)

### !!!! DOUBLE CHECK THIS LINE
#headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}
HEADERS = config.HEADERS
TOTAL_PAGES = config.TOTAL_PAGES


## Storing html files as page#_Y-M-D.html

### ------- SCRAPING THE CONTENT --------

def get_content(url, start_page=1, end_page=1, optional_name=""):
    basic_url = url
    current_date = str(date.today())

    for page_no in range(start_page, end_page+1):
        page_url = basic_url.replace("page=1", f"page={page_no}")
        try:
            req = urllib.request.Request(page_url, headers=HEADERS)
            resp = urllib.request.urlopen(req)
            pageName = config.CONTENT_FOLDER + str(optional_name) + str(page_no) + '_' + current_date + ".html"
            with open(pageName, 'w') as f:
                f.write(resp.read().decode('utf-8'))
                print (pageName, end=" ")
            time.sleep(5) # A03 requires 5 seconds between requests
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print('Too many requests! - SLEEPING')
                print('Restart on page_no: ', page_no)
                print('Restart with url: ', page_url)
                break
            raise
    
    
    ## Once all content is saved in static html files, read them into memory and apply specific functions
    if optional_name == "": # If not collecting user specific page information
        for page_no in range(1, end_page+1):
            pageName = config.CONTENT_FOLDER + str(optional_name) + str(page_no) + '_' + current_date + ".html"
            with open(pageName, 'r', encoding="utf8") as f:
                print("Opening page ", page_no, '...')
                page = f.read()
                basic_stats.process_basic(page, current_date)
        process_articles.process_articles(current_date, start_index=0, start_index2=1)
        # delete page after sending to process
        # process_articles needs the html, so dont delete until then
        print("the html was removed")
        os.remove(pageName)

    
    


if __name__ == "__main__":
    get_content(
        url="https://archiveofourown.org/works/search?commit=Search&page=1&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bquery%5D=&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=hits&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D=",
        start_page=1,
        end_page=TOTAL_PAGES
    )


