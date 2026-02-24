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
import config
import scraping_A03

HEADERS = config.HEADERS

def log_in(username, password):
    # log in as the user
    session = AO3.Session(username, password)
    print(session.is_authed)
    # keep going through pages until there are no more pages left
    
    # If it is expired or you forget to call this function, the error:
    ## AO3.utils.AuthError: Invalid authentication token. Try calling session.refresh_auth_token()
    #session.refresh_auth_token()

    
    # Have to access user information one page at a time, because we want ALL of it,
    # but first need to get first page to find the total number of pages
    
    ## ACCESSING BOOKMARKS
    user_bookmark_url = f"https://archiveofourown.org/users/{username}/bookmarks?page=1"
    scraping_A03.get_content(user_bookmark_url, start_page=1, end_page=1, optional_name="User_Bookmark_")

    ## ACCESSING HISTORY
    user_history_url = f"https://archiveofourown.org/users/{username}/readings?page=1"
    scraping_A03.get_content(user_history_url, start_page=1, end_page=1, optional_name="User_History_")

    ## ACCESSING WORKS
    user_works_url = f"https://archiveofourown.org/users/{username}/works?page=1"
    scraping_A03.get_content(user_works_url, start_page=1, end_page=1, optional_name="User_Works_")



## TAG SEARCHING
##Insert_Tags = None
##page_no = 1


##tag_url = f"https://archiveofourown.org/tags/{Insert_Tags}/works?page={page_no}"

## KEYWORD SEARCHING
##Insert_Keyword = None
##search_url = f"https://archiveofourown.org/works/search?page={page_no}&work_search%5Bquery%5D={Insert_keyword}"



if __name__ == "__main__":
    log_in(
        username=input("Username: "),
        password=input("Password: ")
    )