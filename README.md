# Sentiment Analysis for Movie Reviews

### Description

An end-to-end project with the goal of creating a simple sentiment analysis app that determines whether a user-inputted movie review is positive or negative. The final version of the app can be found [here](https://denzel-movie-sentiment-app.herokuapp.com)

### Background

There are many sites where people can write their own reviews and opinions on newly released movie productions, such as IMDB. Another commonly used review platform is Rotten Tomatoes, which makes use of a binary rating system for its critic reviews; 'fresh' and 'rotten' indicating positive and negative reviews respectively. In general, positive reviews mainly consist of language that suggest a positive sentiment towards the movie and, conversely, negative reviews largely consist of language that suggest a negative sentiment. Using this as inspiration, I decided to try and use machine learning to automate the classification of positive and negative reviews using sentiment analysis.

### Data

This project makes use of a combination of two datasets; a custom web-scraped dataset containing 123,549 user reviews taken from the first 100 movies in IMDB's current [Most Popular list](https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=EPJ9NEX6DE771BWHSG8P&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_2), and the famous [Kaggle IMDB Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews), which contains 50k movie reviews.

The custom scraped dataset was compiled using this [custom Web Scraper script](https://github.com/denzelabad/MovieReview-Sentiment-Analysis/blob/main/IMDB_WebScrape.py)

### Method

