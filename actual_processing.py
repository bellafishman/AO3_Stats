#### Bella Fishman
#### A03 data mining
#### actual_processing.py
# Process articles' CSV files into statistics that I am interested in

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
import config


# weekly trends
## TOP 5 FANDOMS OF THE WEEK


## TOP 1 GROWING FANDOM OF THE WEEK
# stories linked to fandom at beginning of the week vs. now is the largest
# ((total_at_start_of_week - current_total) / total_at_start_of_week) × log10(total_at_start_of_week)
## where current_total > 100



# log in as the user
'''
import AO3
s = AO3.Session(USERNAME, PASSWORD)

and then you use s like any other session: site = s.get(url)

to install the library there uve just got to go:

!pip install ao3_api
'''
s = AO3.Session()
## YOUR FAVORITE FANDOMS OF THE WEEK

## YOUR FAVORITE TAGS OF THE WEEK

## MOST REVISITED WORK

# if any:
## NUMBER OF WORKS WRITTEN

## NUMBER OF TOTAL WORDS WRITTEN

## NUMBER OF HITS RECEIVED

## NUMBER OF BOOKMARKS RECEIVED

## NUMBER OF KUDOS RECEIVED

## HOW MANY OF EACH FANDOM WORK WRITTEN