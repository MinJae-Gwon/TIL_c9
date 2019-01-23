from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask 서버를 사용하기 위한 기초 설정
app = Flask(__name__)

#sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3' #어떤 database를 사용할 것인지
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #

#sqlalchemy 초기화
db = SQLAlchemy(app)

#migrate 초기화
migrate = Migrate(app, db)

#table 만들기
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)

    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
