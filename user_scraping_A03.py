#### Bella Fishman
#### A03 data mining
#### user_scraping_AO3.py
# Use user provided 

import time
import csv
import requests
import urllib
from bs4 import BeautifulSoup, NavigableString
import re
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import AO3
# ----> https://github.com/wendytg/ao3_api
import basic_stats, process_articles
import config

HEADERS = config.HEADERS

def log_in(username, password):
    # log in as the user
    '''
    import AO3
    s = AO3.Session(USERNAME, PASSWORD)

    and then you use s like any other session: site = s.get(url)

    to install the library there uve just got to go:

    !pip install ao3_api
    '''
    session = AO3.Session(username, password)

    # backoff factor is delay between retries
    # connect is number of retries in a connection error event
    retry = Retry(connect=7, backoff_factor=5)

    adapter = HTTPAdapter(max_retries=retry)

    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # keep going through pages until there are no more pages left
    
    # If it is expired or you forget to call this function, the error:
    ## AO3.utils.AuthError: Invalid authentication token. Try calling session.refresh_auth_token()
    session.refresh_auth_token()

    ## ACCESSING BOOKMARKS
    ##username = None
    ##user_bookmark_url = f"https://archiveofourown.org/users/{username}/bookmarks?page={page_no}"

    ## ACCESSING HISTORY
    # has last visited and visited count!!!!!!
    ##username = None
    # Likely need user auth to access, will ask for in app?
    ##user_history_url = f"https://archiveofourown.org/users/{username}/readings?page={page_no}"





if __name__ == "__main__":
    log_in(
        username=input("Username:"),
        password=input("Password:")
    )