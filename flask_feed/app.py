from flask import Flask, render_template, jsonify, request, url_for, flash, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route('/')
def index(filt="."):
    print("index hit")
    if filt:
        print(f"Filter passed: {filt}")
    # Establish connection to mongo
    client = MongoClient("mongodb+srv://luke:dbuserpass@cluster0.z24m3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database("news_feed")
    espn_feed_data = db.espn_news_feed_data
    docs = espn_feed_data.find({"title": { "$regex": filt }})
    return render_template('index.html', posts=docs)


@app.route('/filter/', methods=('GET', 'POST'))
def filter():
    if request.method == 'POST':
        filt = request.form['filter']
        # print(filt)
        if not filt:
            flash('Title is required!')
        else:
            # return redirect(url_for('index', filt=filt))
            return index(filt)
    return render_template('filter.html')