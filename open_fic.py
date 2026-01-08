#### Bella Fishman
#### A03 data mining
#### open_fic.py
# Open the article to get information that is only stored inside the article like specific comments and text

import time
import csv
import requests
import urllib
from bs4 import BeautifulSoup, NavigableString
import re
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import config

HEADERS = config.HEADERS

def open_fic(work_id, headers):
    work_url = f"https://archiveofourown.org{work_id}?view_adult=true&show_comments=true&view_full_work=true"
    #url = 'https://archiveofourown.org' + work_id + '?view_adult=true&view_full_work=true'
    req = urllib.request.Request(work_url, headers=HEADERS)
    resp = urllib.request.urlopen(req)
    print('Successfully opened fiction: ', work_url)
    bs = BeautifulSoup(resp, 'lxml')
    time.sleep(5)
    return bs

# could also get the comments here
# but i dont want to :)