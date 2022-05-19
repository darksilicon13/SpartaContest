# comments.py - 댓글 application

from flask import Blueprint, request, jsonify, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

# 환경 변수 Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')

# users Setup
comments = Blueprint('comments', __name__, url_prefix="/comments")

# MongoDB Atlas Setup - DB: s2lide
client = MongoClient(f'mongodb+srv://{ID}:{PW}@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017)
coll = client.s2lide.comments

# channel을 이용해 전체 댓글 출력
@comments.route('/<channel>', methods=['GET'])
def all_comments(channel):
    comments = list(coll.find({'channel': channel}, {'_id': False}))  # DB에서 전체 댓글 가져오기

    if comments:
        return jsonify({'result': 'SUCCESS', 'comments': comments})    # 댓글이 있으면 댓글을 반환
    return jsonify({'result': 'FAIL', 'msg': '첫 댓글을 달아주세요!'})     # 댓글이 없으면 msg 반환

# 댓글 저장
@comments.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    # 토큰에 저장된 정보 가져오기
    cur_user = get_jwt_identity()
    username = cur_user['username']

    # form 데이터 받아와 변수에 저장
    channel = request.form['channel']
    content = request.form['content']

    # 현재 시간 저장
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    # 댓글 정보 dic 생성
    dic = {
        'channel': channel,
        'content': content,
        'username': username,
        'date': date
    }

    # DB에 댓글 저장 - Collection: comments
    coll.insert_one(dic)

    return redirect(url_for('.all_comments', channel=channel))