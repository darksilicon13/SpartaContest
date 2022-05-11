# users.py - 회원가입 및 로그인 application

from flask import Blueprint, request, redirect, url_for, render_template, session
# from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import json

# users Setup
users = Blueprint('users', __name__, url_prefix="/login")

# MongoDB Setup - 배포할 때 연결
# client = MongoClient('localhost', 27017)
# db = client.S2lide
# 회원 정보 json 데이터 가져와 객체 생성
with open('src/temp.json', "r") as f:
    doc = json.load(f)

# bcrypt Setup
bcrypt = Bcrypt()

@users.route('/')
def login():
    '''
    메인페이지 등에서 로그인 버튼 클릭시 라우터 함수 실행
    로그인 페이지 렌더링 -> 프론트에서 처리?
    '''

# 로그인 페이지에서 로그인 버튼 클릭시 라우터 함수 실행
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

# 로그인 페이지에서 회원가입 버튼 클릭시 라우터 함수 실행
'''
회원가입 페이지 렌더링 -> 프론트?
'''

# 회원가입 페이지에서 register 버튼 클릭시 라우터 함수 실행
@users.route('/register', methods=['POST'])
def register():
    # form 데이터 받아와 변수에 저장
    userName = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirmPassword = request.form['confirmPassword']

    # password와 confirmPassword가 같은지 확인 -> 프론트?
    if password != confirmPassword:
        return {'msg': '비밀번호가 일치하지 않습니다.'}

    # bcrypt 이용해서 비밀번호 암호화 - binary type
    pw_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
    # 회원 정보 객체에 새로운 정보 추가
    doc['users'].append({
        'userName': userName,
        'email': email,
        'password': pw_hash.decode('utf8')  # json 파일로 저장하기 위해 binary 타입을 utf8로 디코드
    })

    # DB에 회원 정보 저장(users collection에 객체 삽입)
    # db.users.insert_one(doc)  #!mongoDB 연결 시 주석 해제
    # 회원 정보 json 파일에 객체 삽입
    with open('src/temp.json', 'w', encoding='utf-8') as f:
        json.dump(doc, f, indent="\t")

    # 회원 가입 완료 시 로그인 페이지로 이동
    return redirect(url_for('home'))    # home -> 로그인 페이지로 수정 필요

# username 확인하는 함수 - 중복체크 버튼 클릭 or focus 옮겨질 때 실행
# 회원가입 시 아이디 중복 체크 / 로그인 시 유저 찾기에 사용
'''
username 변수에 저장
DB에서 username 찾기
    -> 있다면 return true
    -> 없다면 return false
'''