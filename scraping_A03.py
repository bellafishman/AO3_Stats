#### Bella Fishman
#### A03 data mining
#### year in review

import time
import csv
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

### ------- SCRAPING THE CONTENT --------

def get_content(url, start_page=1, end_page=1):
    basic_url = url

    for page_no in range(start_page, end_page+1):
        page_url = basic_url.replace("page=1", f"page={page_no}")
        try:
            req = urllib.request.Request(page_url, headers=HEADERS)
            resp = urllib.request.urlopen(req)
            pageName = config.CONTENT_FOLDER +str(page_no)+".html"
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
    for page_no in range(1, end_page+1):
        pageName = config.CONTENT_FOLDER+str(page_no)+".html"
        with open(pageName, 'r', encoding="utf8") as f:
            print("Opening page ", page_no, '...')
            page = f.read()
            basic_stats.process_basic(page)

    ## Once all basic processing is complete,
    # Complete more processing on articles
    #for page_no in range(1, end_page+1):
    #    pageName = config.CONTENT_FOLDER+str(page_no)+".html"
    #    with open(pageName, 'r', encoding="utf8") as f:
    #        print("Opening page ", page_no, '...')
    #        page = f.read()
    #        bs = BeautifulSoup(page, 'lxml')
    #        articles = bs.find_all('li', {'role':'article'})
    #       process_articles.process_articles(articles, 0, 1)

# url = f"https://archiveofourown.org/tags/{Insert_Tags}/works?page={page_no}"
#url = f"https://archiveofourown.org/works/search?commit=Search&page={start_page}&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bquery%5D=&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=hits&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D="
if __name__ == "__main__":
    get_content(
        url="https://archiveofourown.org/works/search?commit=Search&page=1&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bquery%5D=&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=hits&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D=",
        start_page=1,
        end_page=TOTAL_PAGES
    )


## TAG SEARCHING
##Insert_Tags = None
##page_no = 1


##tag_url = f"https://archiveofourown.org/tags/{Insert_Tags}/works?page={page_no}"

## KEYWORD SEARCHING
##Insert_Keyword = None
##search_url = f"https://archiveofourown.org/works/search?page={page_no}&work_search%5Bquery%5D={Insert_keyword}"

# ACCESSING WORKS
# need to bypass adult content and view work, also see comments?
##Work_ID = None
##work_url = f"https://archiveofourown.org/works/{Work_ID}"

## ACCESSING BOOKMARKS
##username = None
##user_bookmark_url = f"https://archiveofourown.org/users/{username}/bookmarks?page={page_no}"

## ACCESSING HISTORY
# has last visited and visited count!!!!!!
##username = None
# Likely need user auth to access, will ask for in app?
##user_history_url = f"https://archiveofourown.org/users/{username}/readings?page={page_no}"

# through history, it would be great to find all the works a user has kudos'd as well
# it seems to be a gap that a lot of users need and their history contains all seen works so it will surely
# contain all kudos'd works as well. I would have to search through each work in a user's history 
# (time and space dependent on the specific user and how many works they read) to
# find those that have a kudos from the user and compile that into a list.