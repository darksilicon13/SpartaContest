# comments.py - 댓글 application

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
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

# videoId를 이용해 전체 댓글 출력
@comments.route('/', methods=['GET'])
def all_comments():
    videoId = request.args.get('videoId')   # videoId 받아와 변수에 저장
    comments = coll.find({'videoId': videoId}, {'_id': False})  # DB에서 전체 댓글 가져오기

    if comments:
        return jsonify(comments)    # 댓글이 있으면 댓글을 반환
    return jsonify({'msg': '첫 댓글을 달아주세요!'})     # 댓글이 없으면 msg 반환

# 댓글 저장
@comments.route('/upload', methods=['POST'])
def upload():
    # form 데이터 받아와 변수에 저장
    title = request.form['title']
    content = request.form['content']
    username = request.form['username']
    date = datetime.now()

    # 댓글 정보 dic 생성
    dic = {
        title: title,
        content: content,
        username: username,
        date: date
    }

    # DB에 댓글 저장 - Collection: comments
    coll.insert_one(dic)

    # 회원 가입 완료 시 로그인 페이지로 이동
    return jsonify({'msg': '저장을 완료했습니다.'})

# 댓글 수정
@comments.route('/modify', methods=['POST'])
def modify():
    # form 데이터 받아와 변수에 저장
    title = request.form['title']
    content = request.form['content']
    username = request.form['username']
    date = datetime.now.strftime('%Y-%m-%d %H:%M')

    # 댓글 정보 dic 생성
    dic = {
        title: title,
        content: content,
        username: username,
        date: date
    }

    # DB에 댓글 저장 - Collection: comments
    coll.insert_one(dic)

    # 회원 가입 완료 시 로그인 페이지로 이동
    return jsonify({'msg': '저장을 완료했습니다.'})