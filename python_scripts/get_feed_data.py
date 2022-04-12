from pymongo import MongoClient
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import datetime
import feedparser

# References:
# - https://www.geeksforgeeks.org/make-python-api-to-access-mongo-atlas-database/
# - make sure to whitelist your IP
# - https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm
# - flask simple app: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# mongodb://myDBReader:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
# mongodb+srv://cluster0.z24m3.mongodb.net/myFirstDatabase

# Establish connection to mongo
client = MongoClient("mongodb+srv://luke:dbuserpass@cluster0.z24m3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# get db
db = client.get_database("news_feed")

# Connect with collection inside database
espn_feed_data = db.espn_news_feed_data

# sample doc
# personDocument = {
#   "name": { "first": "Alan", "last": "Turing" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }
# sample insertion
# espn_feed_data.insert_one(personDocument)



feed = feedparser.parse("https://www.espn.com/espn/rss/nfl/news")
for entry in feed.entries:
    entry_doc = {
        "published": entry["published"],
        "title": entry["title"],
        "link": entry["link"]
    }
    espn_feed_data.insert_one(entry_doc)



