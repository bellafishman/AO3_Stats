#### Bella Fishman
#### A03 data mining
#### tags_summaries.py
# Getting tags and summaries and fandomss from articles. 

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
from datetime import date


#### ----- adding data and header row to CSV --------
header_row = ['ID', 'Tags', 'Summary', 'Fandoms', 'Date_published', 'Date_Collected']

with open(config.CSV_CONTENT, 'w', encoding='utf8') as f: 
    writer = csv.writer(f)
    writer.writerow(header_row) # write header row to the csv

## GETTING TAGS
def get_tags(article):
    tags = []
    for child in article.find('ul', {'class':'tags commas'}).children:
        if isinstance(child, NavigableString): # skip blank rows
            pass
        else:
            tags.append(child.text.strip())
    return ','.join(tags)

## GETTING SUMMARIES (if available)
def get_summary(article):
    try:
        summary = article.find('blockquote', {'class':'userstuff summary'}).text.strip()
        return summary
    except:
        return ''
    
# GETTING FANDOMS (if available)
# I want to find the most common fandoms:
    # 1. collect all fandoms from each article (distinct)
    # 2. from all fandoms find most common
def get_fandoms(article):
    h5 = article.find('h5', {'class':'fandoms heading'})
    if not h5:
        return 'No fandom'
    
    fandoms = [a.text.strip() for a in h5.find_all('a')]
    # fandoms are split by |, instead we can split but not sure if thats onyl when there are multiple languages for the fandom
    return ','.join(fandoms) if fandoms else 'No fandom'
