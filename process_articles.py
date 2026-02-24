#### Bella Fishman
#### A03 data mining
#### process_articles.py
# Compile information from inside each article like comments, content, and publish date.
# Compile tags, fandoms, and summaries to form comprehensive csv

import time
import csv
import requests
import urllib
from bs4 import BeautifulSoup, NavigableString
import re
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import open_fic, tags_summaries
import config
from datetime import date

TOTAL_PAGES = config.TOTAL_PAGES

HEADERS = config.HEADERS
months = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
### ------ COMPILE INFORMATION INTO CSV ----------
def article_to_row(work_id, article, headers, start_index=1):

    # COMMENTING OUT BECAUSE CLOUDFLARE IS BLOCKING MY REQUESTS TO OPEN INDIVIDUAL ARTICLES
    #bs = open_fic.open_fic(work_id, headers=headers)
    #publish_date = bs.find('dd', {'class':'published'}).text
    # content = bs.find('div', {'id':'chapters'}).text.strip()
    # Collect content here
    # Collect comments here

    # GOING TO USE LAST UPDATED DATE INSTEAD OF PUBLISHED DATE
    last_updated = article.find('p', {'class': 'datetime'}).text.strip()
    # last updated is in form: day# mon year
    # we want form: year-month#-day#
    last_updated = last_updated.split(' ')
    new_last_updated = last_updated[2] + "-" + months[last_updated[1]] + '-' + last_updated[0]


    return [work_id[7:], tags_summaries.get_tags(article), tags_summaries.get_summary(article), tags_summaries.get_fandoms(article), new_last_updated]

def process_articles(current_date, start_index=0, start_index2=1):
    articles = []
    for page_no in range(1, TOTAL_PAGES+1):
        pageName = config.CONTENT_FOLDER + str(page_no) + '_' + current_date + ".html"
        with open(pageName, 'r', encoding="utf8") as f:
            print("Opening page ", page_no, '...')
            page = f.read()
            bs = BeautifulSoup(page, 'lxml')
            page_articles = bs.find_all('li', {'role':'article'})
            articles.extend(page_articles)

    for i, article in enumerate(articles[start_index:]):
        print('Starting processing on article: ', i+start_index2)
        work_id = article.find('h4', {'class':'heading'}).find('a').get('href')
        try: 
            row = article_to_row(work_id, article, HEADERS, start_index2)
            row.append(current_date)
            with open(config.CSV_CONTENT, 'a', encoding='utf8') as f:
                writer = csv.writer(f)
                writer.writerow(row)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print('---Too many requests when accessing article---')
                print('Try ID later: ', work_id, 'current index of', i)
                break
            raise

if __name__ == "__main__":
    process_articles("2026-02-24", start_index=0, start_index2=1)
