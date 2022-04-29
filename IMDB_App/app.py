# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:55:27 2022

@author: denze
"""

from flask import Flask, request, render_template
import pickle
from preprocess import clean_text # Uses same clean_text() function made in the Jupyter Notebook

app = Flask(__name__)

model = pickle.load(open('xgmodel.pkl', 'rb'))
word_vec = pickle.load(open('word_vec.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('IMDB_html.html')

@app.route('/predict', methods= ['POST'])
def predict():
    user_input = request.form['Review']
    clean = clean_text(user_input)
    data = [clean]
    data_vec = word_vec.transform(data)
    prediction = model.predict(data_vec)
    if prediction == 1:
        return render_template('IMDB_html.html',
                               output_text = 'Your review is POSITIVE')
    elif prediction == 0:
        return render_template('IMDB_html.html',
                               output_text = 'Your review is NEGATIVE')

if __name__ == '__main__':
    app.run(debug = False)
                           
    