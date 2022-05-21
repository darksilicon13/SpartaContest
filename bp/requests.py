# requests.py - 사용자 요청 사항 application

from flask import Blueprint, request, jsonify, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

# 환경 변수 Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')

# users Setup
requests = Blueprint('requests', __name__, url_prefix="/requests")
ca = certifi.where()

# MongoDB Atlas Setup - DB: s2lide
client = MongoClient(f'mongodb+srv://{ID}:{PW}@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017, tlsCAFile=ca)
coll = client.s2lide.requests

# 전체 요청사항 출력
@requests.route('/', methods=['GET'])
def all_requests():
    requests = list(coll.find({}, {'_id': False}).sort('date', -1))  # DB에서 전체 요청사항 가져오기

    if requests:
        return jsonify({'result': 'SUCCESS', 'requests': requests})    # 요청사항이 있으면 요청사항 리스트 반환
    return jsonify({'result': 'FAIL', 'msg': 'Tell me the new channel'})     # 요청사항이 없으면 msg 반환

# 요청사항 저장
@requests.route('/upload', methods=['POST'])
def req_upload():
    # form 데이터 받아와 변수에 저장
    chLink = request.form['chLink']
    comment = request.form['comment']

    # 현재 시간 저장
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    # 요청사항 정보 dic 생성
    dic = {
        'chLink': chLink,
        'comment': comment,
        'date': date
    }

    # DB에 저장 - Collection: requests
    coll.insert_one(dic)

    return redirect(url_for('.all_requests'))