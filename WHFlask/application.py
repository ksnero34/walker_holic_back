#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import ssl
import requests
from controller import json_handler
# import sql_connect
import sys
from werkzeug.utils import secure_filename

from model import input_data, select_data

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #


@app.route("/walk_data", methods = ['GET'])
def admin_to_login2():
    data =[ {'id': 1 ,'title':'멸종', 'url' : '대머리'},
	     {'id' : 2, 'title': '이선우', 'url' : 'ㅋㅋ'}]
    return jsonify(data)

@app.route("/input_report_data", methods = ['POST'])
def report_data_to_db():
    type = request.form["type"]
    title = request.form["title"]
    content = request.form["content"]
    image = request.files['image']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    date = request.form['date']
    print(type)
    print(title)
    print(content)
    print(latitude)
    print(longitude)
    print(date)
    image.save("./image", secure_filename(date))
    #이미지 이름 date 로 바꾸기
    input_data.input_report_data(type, title, content, date, latitude, longitude, date)


    return "성공적으로 report_data를 데이터를 넣었습니다."


@app.route("/input_walk_log", methods = ['POST'])
def walk_data_to_db():
    json_data = request.get_json()
    destination = json_data['destination']
    diff = json_data['diff']
    start = json_data['start']
    end = json_data['end']
    
    input_data.input_walk_data(destination, diff, start, end)

    return "성공적으로 walk_data를 넣었습니다."

@app.route("/notice", methods = ["GET"])
def select_():
    return_data = select_data.select_noticeTBL()
    print(return_data)
    print(type(return_data))
# 테스트를위한 주석입니다. 
if __name__ == '__main__':
    app.run( port = 5000)
