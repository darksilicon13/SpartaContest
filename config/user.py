from dotenv import load_dotenv
import os
from pymongo import MongoClient
import pymongo
# 환경 변수 Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')

# MongoDB Atlas Setup

client = pymongo.MongoClient("mongodb+srv://S2lide:0S9fC83ziWkQUq6Y@s2lide.fwsiv.mongodb.net/S2lide?retryWrites=true&w=majority")

db = client.s2lide
