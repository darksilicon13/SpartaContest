# users.py - 회원가입 및 로그인 application

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

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

# DB에서 유저 찾기
def findUser(email):
    return coll.find_one({'email': email}, {'_id': False})

# 로그인 페이지 렌더링
@users.route('/')
def render_login():
    return render_template('login.html')

# 유저 로그인
@users.route('/login', methods=['POST'])
def login():
    # form 데이터 받아와 변수에 저장
    email = request.form['email']
    password = request.form['password']

    user = findUser(email)  # DB에서 사용자 정보 받아와 user에 저장

    # 유저 정보가 있고 비밀 번호가 일치하는지 검사
    if user and bcrypt.check_password_hash(user['password'], password):
        # 로그인 성공 시 토큰 생성
        token = create_access_token(identity={'email': user['email'], 'username': user['username']}, expires_delta=timedelta(hours=8))

        # 쿠키에 토큰 저장 후 main.html로 이동
        res = make_response(jsonify({'result': 'SUCCESS', 'msg': user['username']+' 님으로 로그인 되었습니다.'}))
        res.set_cookie('token', token)

        return res

    return jsonify({'result': 'FAIL', 'msg': '아이디 혹은 비밀번호를 다시 확인해주세요.'})   # FAIL과 msg 반환

# 유저 로그아웃
@users.route('/logout', methods=['POST'])
def logout():
    # 쿠키에서 token 삭제하고 home으로 이동
    res = make_response(redirect('home'))
    res.delete_cookie('token')

    return res

# 회원 가입 페이지 렌더링
@users.route('/join')
def render_join():
    return render_template('register.html')

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
    return jsonify({'result': 'SUCCESS'})

# 이메일 중복 확인
@users.route('/check', methods=['GET'])
def check():
    email = request.args.get('email')     # 전달 받은 데이터 변수에 저장

    user = findUser(email)  # DB에서 데이터 찾기

    if not user:
        return jsonify({'result': 'SUCCESS'})    # DB에 데이터가 없으면 SUCCESS 반환

    return jsonify({'result': 'FAIL'})   # DB에 데이터가 있으면 FAIL 반환