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


# ----- For General Information: -------

# weekly trends
## TOP 5 FANDOMS OF THE WEEK


## TOP 1 GROWING FANDOM OF THE WEEK
# stories linked to fandom at beginning of the week vs. now is the largest
# ((total_at_start_of_week - current_total) / total_at_start_of_week) × log10(total_at_start_of_week)
## where current_total > 100

## Top Day and time for reader to read

## Top Day and time for all readers to read (hits received)



# ----- For User Information: -------

## YOUR FAVORITE FANDOMS OF THE WEEK

## YOUR FAVORITE TAGS OF THE WEEK

## MOST REVISITED WORK

# through history, it would be great to find all the works a user has kudos'd as well
# it seems to be a gap that a lot of users need and their history contains all seen works so it will surely
# contain all kudos'd works as well. I would have to search through each work in a user's history 
# (time and space dependent on the specific user and how many works they read) to
# find those that have a kudos from the user and compile that into a list.

# if any:
## NUMBER OF WORKS WRITTEN

## NUMBER OF TOTAL WORDS WRITTEN

## NUMBER OF HITS RECEIVED

## NUMBER OF BOOKMARKS RECEIVED

## NUMBER OF KUDOS RECEIVED

## HOW MANY OF EACH FANDOM WORK WRITTEN

