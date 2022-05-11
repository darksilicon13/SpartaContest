# app.py - main application

from flask import Flask, render_template, session
from bp.users import users

#Flask App Setup
app = Flask(__name__)

# BluePrint Setup
app.register_blueprint(users)   # 로그인 및 회원 가입

@app.route('/')
def home():
    return render_template('main.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)