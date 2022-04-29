# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:58:06 2022

@author: denze
"""

import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stpwrds = set(stopwords.words('english'))

def remove_punc(text):
    # Replace sentence-ending punctuation with whitespace
    text = text.replace('.', ' ')
    text = text.replace('!', ' ')
    text = text.replace('?', ' ')
    # Replace commas and brackets with whitespace
    text = text.replace(',', ' ')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    # Replace word-dividing punctuation with whitespace to separate words
    text = text.replace('/', ' ')
    text = text.replace('-', ' ')
    # Remove the remaining punctuation from the reviews
    text = text.translate(str.maketrans('','', string.punctuation))
    return text

def fix_space(text):
    # Fix double spaces caused by replacing punctuation, and any other weird spaces
    text = text.split()
    text = " ".join(text)
    return text

def remove_html(text):
    # Remove html line breaks
    text = text.replace('<br />', '')
    # Remove all other possible html
    pattern = re.compile('<.*?>')
    text = pattern.sub(r'', text)
    return text

def remove_stopwords(text):
    # Remove common stopwords
    text = " ".join([string for string in str(text).split() if string not in stpwrds])
    return text

def lemmatize(text):
    # Convert words to their original lemma
    text = " ".join([WordNetLemmatizer().lemmatize(word) for word in text.split()])
    return text

def clean_text(text):
    text = text.lower()
    text = remove_html(text)
    text = remove_punc(text)
    text = fix_space(text)
    text = remove_stopwords(text)
    text = lemmatize(text)
    return text