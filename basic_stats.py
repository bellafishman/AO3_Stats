#### Bella Fishman
#### A03 data mining
#### basic_stats
# get basic stats like title, author, ID, date updated, rating, pairing, warning,
# completion status, languages, word count, chapters, comments, kudos, bookmarks, hits

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

# each page has a max of 20 works

# link structure:
# 'https://archiveofourown.org/tags/Fluff/works'
# 'https://archiveofourown.org/tags/Alternate%20Universe/works'
# 'https://archiveofourown.org/tags/Alternate%20Universe/works?page=2'
# initiate new file:
header = ['Title', 'Author', 'ID', 'Date_updated', 'Rating', 'Pairing', 'Warning', 'Complete',
            'Language', 'Word_count', 'Num_chapters', 'Num_comments', 'Num_kudos', 
            'Num_bookmarks', 'Num_hits']

with open(config.CSV_BASIC, 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(header)


def process_basic(page_content):
    bs = BeautifulSoup(page_content, 'lxml')
    titles=[]
    authors=[]
    IDs=[]
    date_updated=[]
    ratings=[]
    pairings=[]
    warnings=[]
    complete=[]
    languages=[]
    word_count=[]
    chapters=[]
    comments=[]
    kudos=[]
    bookmarks=[]
    hits=[]

    for article in bs.find_all('li', {'role':'article'}):
        titles.append(article.find('h4', {'class':'heading'}).find('a').text)
        try:
            authors.append(article.find('a', {'rel':'author'}).text)
        except:
            authors.append('Anonymous')
        IDs.append(article.find('h4', {'class':'heading'}).find('a').get('href')[7:])
        date_updated.append(article.find('p', {'class':'datetime'}).text)
        ## uses regex (re.compile) to find string matching rating-(any chars of any length (.*)) rating
        ratings.append(article.find('span', {'class':re.compile(r'rating\-.*rating')}).text)
        pairings.append(article.find('span', {'class':re.compile(r'category\-.*category')}).text)
        warnings.append(article.find('span', {'class':re.compile(r'warning\-.*warnings')}).text)
        complete.append(article.find('span', {'class':re.compile(r'complete\-.*iswip')}).text)
        languages.append(article.find('dd', {'class':'language'}).text)
        count = article.find('dd', {'class':'words'}).text
        if len(count) > 0:
            word_count.append(count)
        else:
            word_count.append('0')
        chapters.append(article.find('dd', {'class':'chapters'}).text.split('/')[0]) # getting left half of (x/y)
        ## comments is not present as an option if there are no comments
        try:
            comments.append(article.find('dd', {'class':'comments'}).text)
        except: 
            comments.append('0')
        try:
            kudos.append(article.find('dd', {'class':'kudos'}).text)
        except:
            kudos.append('0')
        try:
            bookmarks.append(article.find('dd', {'class':'bookmarks'}).text)
        except: 
            bookmarks.append('0')
        try:
            hits.append(article.find('dd', {'class':'hits'}).text)
        except:
            hits.append('0')
    
    df = pd.DataFrame(list(zip(titles, authors, IDs, date_updated, ratings, pairings, warnings, complete, languages, 
                               word_count, chapters, comments, kudos, bookmarks, hits)))
    print('Successfully processed', len(df), 'rows.')

    with open(config.CSV_BASIC, 'a', encoding='utf8') as f:
        df.to_csv(f, header=False, index=False)
    temp = pd.read_csv(config.CSV_BASIC)
    print('Now there is a total of ', len(temp), 'rows of data.')
    print('================================================')



