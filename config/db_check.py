# from dotenv import load_dotenv
# import os
from pymongo import MongoClient
import certifi         
ca = certifi.where()   

# 환경 변수 Setup
# load_dotenv()
# ID = os.getenv('DB_ID')
# PW = os.getenv('DB_PW')

# MongoDB Atlas Setup
client = MongoClient(f'mongodb+srv://S2lide:0S9fC83ziWkQUq6Y@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017, tlsCAFile=ca)
db = client.s2lide

links = list(db.link.find({},{'_id':False}))[0]
print(links)
# db.link.delete_many({})
