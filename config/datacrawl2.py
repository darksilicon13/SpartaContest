from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import app
# app.py - main application

from flask import Flask, render_template, session,jsonify,request
from pymongo import MongoClient
from dotenv import load_dotenv
import os
#Flask App Setup
app = Flask(__name__)

#MongoDB Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')

# MongoDB Atlas Setup
client = MongoClient(f'mongodb+srv://{ID}:{PW}@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017)
db = client.s2lide
channels = list(db.link.find({},{'_id':False}))
for i in channels:
    channel = i['채널명']
    browser = webdriver.Chrome()
    url = 'https://www.youtube.com/results?search_query=' + channel
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "lxml")  # HTML을 "lxml"로 파싱(해석)
    channel_url = soup.find('a', attrs={'class': "channel-link yt-simple-endpoint style-scope ytd-channel-renderer"})[
        'href']
    url='http://www.youtube.com'+channel_url
    browser.get(url)
    browser.maximize_window()
    soup = BeautifulSoup(browser.page_source, "lxml")
    movie = soup.find_all('a', attrs={'id': 'video-title',
                                      'class': 'yt-simple-endpoint style-scope ytd-grid-video-renderer'})
    for i in movie:
        doc={
            '채널명':channel,
            'videoId':i['href'].strip('/watch?v=')
        }
        db.videoId.insert_one(doc)
    browser.quit()

#
# list_all_row = []  # 전체 내용을 넣을 리스트