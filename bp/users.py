# users.py - 회원가입 및 로그인 application

from flask import Blueprint, render_template, request, jsonify ,redirect, url_for, session
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt

# 환경 변수 Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')

# users Setup
users = Blueprint('users', __name__, url_prefix="/user")

# MongoDB Atlas Setup - DB: s2lide
client = MongoClient(f'mongodb+srv://{ID}:{PW}@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017)
coll = client.s2lide.users

# bcrypt Setup
bcrypt = Bcrypt()

# 로그인 페이지 렌더링
@users.route('/')
def render_login():
    return render_template('main.html')

# 유저 로그인
@users.route('/login', methods=['GET'])
def login():
    email = request.form['email']
    password = request.form['password']

    result = find()

    if result.result:
        db_pw = result.user[0].password
        if bcrypt.check_password_hash(db_pw, password):
            # 세션에 유저정보 저장
            return jsonify({'status': 'SUCCESS', 'msg': '로그인 성공!'})
        return jsonify({'status': 'FAIL', 'msg': '비밀번호가 틀렸습니다.'})

    return jsonify({'status': 'FAIL', 'msg': '유저 정보가 없습니다.'})

# 회원 가입 페이지 렌더링
@users.route('/join')
def render_join():
    return render_template('main.html')

# DB에 유저 정보 등록 - 회원 가입
@users.route('/register', methods=['POST'])
def register():
    # form 데이터 받아와 변수에 저장
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # bcrypt 이용해서 비밀번호 암호화 - binary type
    pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    # 회원 정보 dic 생성
    dic = {
        'username': username,
        'email': email,
        'password': pw_hash
    }

    # DB에 회원 정보 저장 - Collection: users
    coll.insert_one(dic)

    # 회원 가입 완료 시 로그인 페이지로 이동
    return redirect(url_for('.render_login'))

# 유저 찾기 - 중복 확인 및 로그인
@users.route('/find', methods=['GET'])
def find():
    email = request.args.get('email')     # 전달 받은 데이터 변수에 저장

    # DB에서 데이터 찾기
    user = coll.find_one({'email': email}, {'_id': False})

    if not user:
        return jsonify({'result': False})    # DB에 데이터가 없으면 False 반환

    return jsonify({'result': True, 'user': user})   # DB에 데이터가 있으면 True와 user 반환