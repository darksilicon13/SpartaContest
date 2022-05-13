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

    # MongoDB Atlas Setup

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

    # 스크롤 끝까지 내리기(내리고싶지 않다면 반복문 삭제)*********************************************************
    # while True:
    #     # 현재 scrollHeight 값 가져오기
    #     init_height = browser.execute_script("return document.documentElement.scrollHeight")
    #     # 평소 사용하던 documnet.body.scrollHeight는 값이 반환되지 않음.
    #     # 유튜브 페이지에는 스크롤을 내릴 수 있는 곳이 두 개여서 그런듯..?!
    #
    #     # 현재 scrollHeight 값 만큼 스크롤 아래로 내리기
    #     browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
    #
    #     # 웹드라이버 동작 기다리기
    #     # 소수를 쓰는 이유는 로봇 처럼 안보여야 차단 안될것 같아서
    #     time.sleep(random.uniform(1, 2))
    #
    #     # 변경된 scrollHeight 값 가져오기
    #     curr_height = browser.execute_script("return document.documentElement.scrollHeight")  # 변경된 scrollHeight 값 가져오기
    #     # 이전과 현재 scrollHeight 값 비교하여 같은 경우는 스크롤의 끝이란 뜻이기 때문에 반복문 탈출하기
    #     if init_height == curr_height:
    #         break


    soup = BeautifulSoup(browser.page_source, "lxml") #HTML을 "lxml"로 파싱(해석)



    # 영상 제목에 해당하는 태그'들' 모두 가져오기
    title_all = soup.find_all("div", attrs={"class": "ChannelListCardBig_title__1c0m6"})
    thumbnail = soup.find_all("img", attrs={"class": "ChannelListCardBig_videoClipImg__2x2XH",'alt':'img'})
    youtubericon=soup.find_all('img',attrs={'class':'ChannelListCardSmall_thumbnailsImg__2mQXY'})
    # channel=soup.select("a",attrs={'class':'ChannelListCardBig_linkImg__1VnmG'})
    # for j in channel:
    #     if('youtube' in j['href']):
    #         print(j['href'])
    list_all_row = []  # 전체 내용을 넣을 리스트
    # 리스트에 추가<img class="" src="https://yt3.ggpht.com/AVvSUTGMUTesviGa0cMbvGkmROd3XCTyR7iobZ5icit4pAUz8ePmaQdh4chhTz_2AomGjiJu5A=s800-c-k-c0x00ffffff-no-rj" alt="흔한남매">
    for title in title_all:
        for i in youtubericon:
            for s in thumbnail:
                list_row = []  # for문 안에서 가져와지는 내용을 넣을 리스트
                list_row.append(key)
                list_row.append(title.get_text())  # 영상 제목
                list_row.append(s['src'])
                list_row.append(i['src'])
                list_all_row.append(list_row)  # 영상 순서, 제목, 링크 list_all_row에 넣기




    # CSV파일 만들기
    dataframe = pd.DataFrame(list_all_row,columns=['키워드','채널명','썸네일','유튜버아이콘'])  # 데이터 프레임으로 변환
    # date_today = datetime.now().strftime("%Y%m%d")  # 오늘 날짜 구하기. 파일 제목 설정을 위함
    # dataframe.to_csv(f"{date_today}PlayList.csv", encoding="utf-8-sig")  # csv 파일로 저장
    # 웹브라우저 종료
    browser.quit()
    # df=pd.read_csv('20220513PlayList.csv')#오늘 날짜 넣기
    df1=dataframe['채널명'].unique()
    dataframe.drop_duplicates(subset='썸네일',inplace=True)
    dataframe['채널명']=df1
    # for i in youtubericon:
    #     dataframe['유튜버이미지'][i.index()]=i['src']
    for i in range(0,len(dataframe['채널명'])):
        doc={
            '키워드':dataframe['키워드'][i],
            '채널명':dataframe['채널명'][i],
            '썸네일':dataframe['썸네일'][i],
            '유튜버아이콘':dataframe['유튜버아이콘'][i]
        }
        db.link.insert_one(doc)
