from selenium import webdriver
import time
import random
# 웹브라우저 작동을 기다리기 위한 라이브러리
# 처리속도가 너무 빠른 경우 정보가 호출되기 전에 프로그램이 실행되어 오류가 발생할 수도 있음
# 아래 라이브러리 대신 Selenium 라이브러리의 "WebDriverWait, By, expected_conditions" 모듈을 써도 됨
# 프로그램 사용법**************************************************************************
# 1. 자신의 버전에 맞는 크롬드라이버를 설치 크롬버전 확인은 크롬 설정 - chrome 정보에서 확인
# https://chromedriver.chromium.org/downloads 에서 다운 가능
# 2.링크 입력


# HTML Pasrsing을 위한 라이브러리
# 동적 페이지에서 HTML 정보를 가져온 후 BeautifulSoup 모듈로 해석
from bs4 import BeautifulSoup

# csv 파일 저장을 위한 라이브러리
import pandas as pd

# 시간 관련 라이브러리
# 최종 파일에 오늘의 날짜를 입력하기 위함
from datetime import datetime, timedelta  # 현재 시간
from pytz import timezone  # 한국 기준 시간
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import pymongo
# 환경 변수 Setup
keyword=['고양이','강아지','Vlog','일상','영화','애니','음악','여행','ASMR','FUN']
for key in keyword:
    load_dotenv()
    ID = os.getenv('DB_ID')
    PW = os.getenv('DB_PW')

    client = pymongo.MongoClient("mongodb+srv://S2lide:0S9fC83ziWkQUq6Y@s2lide.fwsiv.mongodb.net/S2lide?retryWrites=true&w=majority")

    db = client.s2lide

    # 웹브라우저 작동
    browser = webdriver.Chrome()

    # url변수에 유튜버별 동영상 목록 페이지 링크 입력 *********************************************
    url = "https://vling.net/search?keyword="+key
    # URL 열기
    browser.get(url)
    # Chrome 창 최대화
    browser.maximize_window()

    soup = BeautifulSoup(browser.page_source, "lxml") #HTML을 "lxml"로 파싱(해석)

    # 영상 제목에 해당하는 태그'들' 모두 가져오기
    title_all = soup.find_all("div", attrs={"class": "ChannelListCardBig_title__1c0m6"})
    thumbnail = soup.find_all("img", attrs={"class": "ChannelListCardBig_videoClipImg__2x2XH",'alt':'img'})
    youtubericon=soup.find_all('img',attrs={'class':'ChannelListCardSmall_thumbnailsImg__2mQXY'})

    list_all_row = []  # 전체 내용을 넣을 리스트

    for i in range(0, len(title_all)):
        list_row = []  # for문 안에서 가져와지는 내용을 넣을 리스트
        list_row.append(key)
        list_row.append(title_all[i].get_text())  # 영상 제목
        list_row.append(thumbnail[i]['src'])
        list_row.append(youtubericon[i]['src'])
        list_all_row.append(list_row)  # 영상 순서, 제목, 링크 list_all_row에 넣기

    browser.quit()

    for i in range(0,len(list_all_row)):
        doc={
            '키워드':list_all_row[i][0],
            '채널명':list_all_row[i][1],
            '썸네일':list_all_row[i][2],
            '유튜버아이콘':list_all_row[i][3]
        }
        db.link.insert_one(doc)
