# users.py - 회원가입 및 로그인 application

from flask import Blueprint, render_template, request, redirect, url_for, session
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

# MongoDB Atlas Setup
client = MongoClient(f'mongodb+srv://{ID}:{PW}@s2lide.fwsiv.mongodb.net/?retryWrites=true&w=majority', 27017)
db = client.s2lide

# bcrypt Setup
bcrypt = Bcrypt()

# 로그인 페이지 렌더링
@users.route('/')
def render_login():
    return render_template('login.html')

# 로그인 페이지에서 로그인 버튼 클릭시 라우터 함수 실행
@users.route('/login', methods=['GET'])
def login():
    '''
    username, password 모두 입력됐을 경우만 라우터 함수 실행 -> 프론트 처리?

    username, password 변수에 저장
    비밀번호 암호화

    DB에서 username 찾기(함수)
        -> 없으면 return "사용자 정보가 없습니다."
    찾은 데이터의 password와 입력받은 password가 같은지 확인
        -> 같다면 세션에 username 저장 후 return 메인 페이지로 이동
        -> 다르다면 return "비밀번호가 틀렸습니다."

    bcrypt.checkpw("password".encode("utf-8"), pw_hash)
    # 즉 password 라는 비밀번호를 암호화하고, 이후에 체크하는 작업을 할때 해당 메소드를 통해 일치여부 확인 가능
    '''

# 회원 가입 페이지 렌더링
@users.route('/join')
def render_join():
    return render_template('join.html')

# DB에 유저 정보 등록 - 회원 가입
@users.route('/register', methods=['POST'])
def register():
    # form 데이터 받아와 변수에 저장
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # bcrypt 이용해서 비밀번호 암호화 - binary type
    pw_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
    # 회원 정보 객체에 새로운 정보 추가
    doc = {
        'username': username,
        'email': email,
        'password': pw_hash
    }
    '''
    doc['users'].append({
        'username': username,
        'email': email,
        'password': pw_hash.decode('utf8')  # json 파일로 저장하기 위해 binary 타입을 utf8로 디코드
    })
    '''

    # DB에 회원 정보 저장(users collection에 객체 삽입)
    db.user.insert_one(doc)  #!mongoDB 연결 시 주석 해제
    # 회원 정보 json 파일에 객체 삽입
    #with open('src/temp.json', 'w', encoding='utf-8') as f:
    #    json.dump(doc, f, indent="\t")

    # 회원 가입 완료 시 로그인 페이지로 이동
    return redirect(url_for('home'))    # home -> 로그인 페이지로 수정 필요

# 유저 찾기 - 중복 확인 및 로그인
@users.route('/find', methods=['GET'])
def find():
    email = request.args.get('email')     # 전달 받은 데이터 변수에 저장

    # DB에서 데이터 찾기
    user = list(db.user.find({'email': email}, {'_id': False}))
    if not user:
        return {'result': False}    # DB에 데이터가 없으면 False 반환

    return {'result': True, 'user': user}   # DB에 데이터가 있으면 True와 user 반환