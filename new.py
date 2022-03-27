import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN: #如果是Windows系统，使用三个斜线
    prefix = 'sqlite:///'
else:   #否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # 关闭对模型修改的监控
# 在拓展类实例化前加载配置
db = SQLAlchemy(app)

class User(db.Model):   # 表名将会是user（自动生成， 小写处理）
    id = db.Column(db.Integer, primary_key = True) # 主键
    name = db.Column(db.String(20)) # 名字

class Movie(db.Model):  # 表名将会是movie
    id = db.Column(db.Integer, primary_key=True)    # 主键
    title = db.Column(db.String(60))    # 电影标题
    year = db.Column(db.String(4))  # 电影年份