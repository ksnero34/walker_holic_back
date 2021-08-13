#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import ssl
import requests
from controller import json_handler
# import sql_connect
import sys
from werkzeug.utils import secure_filename
import os
from model import input_data, select_data
folder_name = "./image"
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #


# form 형식으로 받음
@app.route("/input_report_data", methods = ['POST'])
def report_data_to_db():
    type = request.form["type"]
    title = request.form["title"]
    content = request.form["content"]
    image = request.files['image']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    date = request.form['date']
 
    image.save(os.path.join("./image", secure_filename(date)))
    #이미지 이름 date 로 바꾸기
    input_data.input_report_data(type, title, content, date+".jpg", latitude, longitude, date)


    return "성공적으로 report_data를 데이터를 넣었습니다."

# json형식으로 받음
@app.route("/input_walk_log", methods = ['POST'])
def walk_data_to_db():
    json_data = request.get_json()
    destination = json_data['destination']
    diff = json_data['diff']
    start = json_data['start']
    end = json_data['end']
    
    input_data.input_walk_data(destination, diff, start, end)

    return "성공적으로 walk_data를 넣었습니다."


# select 부분
@app.route("/notice", methods = ["GET"])
def select_():
    return_data = select_data.select_noticeTBL()
    json_form = {"id" : 0, "title" : "", "url" : ""}
    return_select_data = []
    for index in range(len(return_data)):
        json_form["id"] = return_data[index][0]
        
        json_form["title"] = return_data[index][1]
        
        json_form["url"] = return_data[index][2]
        return_select_data.append(dict(json_form))

    return jsonify(return_select_data)

# select 부분
@app.route("/issue", methods = ["GET"])
def select_2():
    return_data2 = select_data.select_issue()
    json_form2 = {"id" : 0, "title" : "", "url" : ""}
    return_select_data2 = []
    for index in range(len(return_data2)):
        json_form2["id"] = return_data2[index][0]
        
        json_form2["title"] = return_data2[index][1]
        
        json_form2["url"] = return_data2[index][2]
        return_select_data2.append(dict(json_form2))

    return jsonify(return_select_data2)


if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000)
