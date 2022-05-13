from selenium import webdriver

from bs4 import BeautifulSoup

import pandas as pd

browser = webdriver.Chrome()
key='고양이'
url = "https://vling.net/search?keyword=" + key

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


soup = BeautifulSoup(browser.page_source, "lxml")  # HTML을 "lxml"로 파싱(해석)

# 영상 제목에 해당하는 태그'들' 모두 가져오기
# title_all = soup.find_all("div", attrs={"class": "ChannelListCardBig_title__1c0m6"})
# thumbnail = soup.find_all("img", attrs={"class": "ChannelListCardBig_videoClipImg__2x2XH", 'alt': 'img'})
youtubericon=soup.find_all('img',attrs={'class':'ChannelListCardSmall_thumbnailsImg__2mQXY'})
# channel=soup.select("a",attrs={'class':'ChannelListCardBig_linkImg__1VnmG'})
print(youtubericon[0]['src'])
# list_all_row = []  # 전체 내용을 넣을 리스트
browser.quit()