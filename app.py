# app.py - main application

from flask import Flask, render_template, session, jsonify, request
from bp.users import users
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os
ca = certifi.where()
#Flask App Setup
app = Flask(__name__)

#MongoDB Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')

# BluePrint Setup
app.register_blueprint(users)   # 로그인 및 회원 가입

# MongoDB Atlas Setup
client = MongoClient(f'mongodb+srv://{ID}:{PW}@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017, tlsCAFile=ca)
db = client.s2lide

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/playlist', methods=['GET'])
def db_to_playlist():
    dbjson = list(db.videoId.find({},{'_id':False}))
    return render_template('playlist.html')

@app.route('/request')
def request():
    return render_template('request.html')

# 쿼리 파라미터 받기
@app.route('/data', methods=['GET'])
def db_to_main():
    dbjson = list(db.link.find({},{'_id':False}))
    return jsonify({'msg': dbjson})

@app.route('/movie', methods=['GET'])
def playlist():
    dbjson = list(db.videoId.find({'채널명':request.args.get('channel')},{'_id':False}))
    return jsonify({'msg': dbjson})
# @app.route('/')
# def home():
#     #로그인 상태에 따라 index 로딩시 상태변수 전달 / 로그인페이지 => 로그아웃으로 변경
#     logged = False
#     if "user_id" in session:
#         logged = True
#     return render_template('register.html', logged = logged)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)