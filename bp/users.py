# users.py - 회원가입 및 로그인 application

from flask import Blueprint, render_template, request, jsonify ,redirect, url_for, session
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta

# 환경 변수 Setup
load_dotenv()
ID = os.getenv('DB_ID')
PW = os.getenv('DB_PW')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

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
    return render_template('main.html')

# 유저 로그인
@users.route('/login', methods=['POST'])
def login():
    # form 데이터 받아와 변수에 저장
    email = request.form['email']
    password = request.form['password']

    user = findUser(email)  # DB에서 사용자 정보 받아와 user에 저장

    if user:    # 유저 정보가 있으면 비밀번호 비교
        if bcrypt.check_password_hash(user['password'], password):
            # 비밀번호 일치하면 토큰 생성
            payload = {
                'email': email,
                'exp': datetime.utcnow() + timedelta(hours=8)   # 로그인 8시간 유지
            }
            token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

            return jsonify({'result': 'SUCCESS', 'token': token})   # SUCCESS와 토큰 반환

        return jsonify({'result': 'FAIL', 'msg': '비밀번호가 틀렸습니다.'})   # FAIL과 msg 반환

    return jsonify({'result': 'FAIL', 'msg': '유저 정보가 없습니다.'})   # FAIL과 msg 반환

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

# 이메일 중복 확인
@users.route('/check', methods=['GET'])
def check():
    email = request.args.get('email')     # 전달 받은 데이터 변수에 저장

    # DB에서 데이터 찾기
    user = findUser(email)

    if not user:
        return jsonify({'result': False})    # DB에 데이터가 없으면 False 반환

    return jsonify({'result': True})   # DB에 데이터가 있으면 True 반환

# 사용자 인증 - 토큰 확인
@users.route('/auth', methods=['GET'])
# @jwt_required()   # 토큰이 없으면 함수에 접근 불가
def auth():
    return
    # 토큰 확인
	# cur_user = get_jwt_identity() # 이전에 발행한 토큰 가져오기
	# if cur_user is None:
	# 	return "User Only!"
	# else:
	# 	return "Hi!," + cur_user