# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:45:35 2022

@author: denzel
"""

import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
ID = []
review = []
rating = []
# Get IDs of the current top 100 Most Popular movies
URL_List = "https://www.imdb.com/chart/moviemeter?sort=rk,asc&mode=simple&page=1"
page = requests.get(URL_List)
soup = bs(page.content, "html.parser")
lister_list = soup.find(class_ = 'lister-list')
movies = lister_list.find_all(class_ = 'watchlistColumn')
for i in movies:
    x = i.findChildren(recursive = False)
    ID.append(str(x[0].get('data-tconst')))
sel_path = "chromedriver.exe"
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(sel_path, options = options)
for code in ID:
    # Begin scraping through the webpage of each movie
    URL = "https://www.imdb.com/title/" + code + "/reviews?ref_=tt_urv"
    page2 = requests.get(URL)
    soup2 = bs(page2.content, "html.parser")
    driver.get(URL)
    # Get the total number of user reviews for the movie
    lister = soup2.find(class_ = 'lister')
    header = lister.find(class_ = 'header').span.text
    # Separate text from total and convert to int
    total = int(header.split(' ')[0].replace(',', ''))
    total_clicks = total//25 # Total number of clicks until the full page is loaded
    try:
        for i in range(total_clicks):
            load = driver.find_element_by_id('load-more-trigger')
            load.click()
            time.sleep(4)
    except:
        break
    full = bs(driver.page_source, "html.parser") # Open full page with beautifulsoup
    review_container = full.find_all(class_ = 'review-container')
    for i in review_container:
        # Add ratings
        parent = i.find('span', class_ = 'rating-other-user-rating')
        if parent == None:
            rating.append(None)
        else:
            child = parent.findChildren('span', recursive = False)
            rating.append(int(child[0].text))
        # Add reviews
        x = i.find(class_ = 'text show-more__control')
        if x == None:
            y = i.find(class_ = 'text show-more__control clickable')
            review.append(y.text)
        else:
            review.append(x.text)
    time.sleep(10)
# Aggregate into csv file
raw_reviews = pd.DataFrame({
    'Review': review,
    'Rating': rating})
raw_reviews.to_csv('raw_reviews_IMDB2.csv')