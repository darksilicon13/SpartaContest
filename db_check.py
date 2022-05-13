from dotenv import load_dotenv
import os
from pymongo import MongoClient
# 환경 변수 Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')

# MongoDB Atlas Setup
client = MongoClient(f'mongodb+srv://{ID}:{PW}@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017)
db = client.s2lide

# links = list(db.link.find({},{'_id':False}))
db.link.delete_many({})
