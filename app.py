# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:57:08 2021

@author: IT City
"""

from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from twitterAPImachine import get_related_tweets


pipeline = load("text_classification_decisiontree.joblib")


def requestResults(name):
    tweets = get_related_tweets(name)
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
    data = str(tweets.prediction.value_counts()) + '\n\n'
    return data + str(tweets) + "arslan is my name"
    



app = Flask(__name__ , template_folder='https://github.com/arslanbhatti016/flask-twitter-api/tree/main/template')
@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "




if __name__ == '__main__':
    app.run(debug = False)
