import pandas as pd

import pymongo


# MongoDB Atlas Setup

client = pymongo.MongoClient("mongodb+srv://S2lide:0S9fC83ziWkQUq6Y@s2lide.fwsiv.mongodb.net/S2lide?retryWrites=true&w=majority")

db = client.s2lide

df=pd.read_csv('20220511PlayList.csv') #csv파일명 지정

for i in range(0, len(df)):
    doc = {
        '제목': df['제목'][i],
        '링크': df['링크'][i],
        '유튜버': df['유튜버 이름'],
        '썸네일': df['썸네일링크']
    }
    db.link.insert_one(doc)