# app.py - main application

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import certifi
import os

from bp.users import users
from bp.comments import comments
from bp.requests import requests

# Flask App Setup
app = Flask(__name__)
ca = certifi.where()
app.config.update(
    DEBUG = True,
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
)
jwt = JWTManager(app)

# 환경변수 Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')

# MongoDB Atlas Setup
client = MongoClient(f'mongodb+srv://{ID}:{PW}@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017, tlsCAFile=ca)
db = client.s2lide

# BluePrint Setup
app.register_blueprint(users)   # 로그인 및 회원 가입
app.register_blueprint(comments)   # 댓글
app.register_blueprint(requests)   # 사용자 요청 사항

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/playlist', methods=['GET'])
def db_to_playlist():
    return render_template('playlist.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/customer_request')
def customerequest():
    return render_template('request.html')

@app.route('/about')
def about():
    return render_template('about.html')

# 쿼리 파라미터 받기
@app.route('/data', methods=['GET'])
def db_to_main():
    dbjson = list(db.link.find({},{'_id':False}))
    return jsonify({'msg': dbjson})

@app.route('/movie', methods=['GET'])
def playlist():
    dbjson = list(db.videoId.find({'채널명': request.args.get('channel')}, {'_id': False}))
    return jsonify({'msg': dbjson})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)