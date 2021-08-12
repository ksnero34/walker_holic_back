#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import ssl
import requests
from controller import json_handler
# import sql_connect
import sys
from werkzeug.utils import secure_filename

from model import input_data

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
    image.save(secure_filename(image.filename))

    input_data.input_report_data(type, title, content, image.filename, latitude, longitude, date)


    return "hello"


@app.route("/input_walk_log", methods = ['POST'])
def walk_data_to_db():
    json_data = request.get_json()
    destination = json_data['destination']
    diff = json_data['diff']
    start = json_data['start']
    end = json_data['end']

    input_data.input_walk_data(destination, diff, start, end)

    return "hello"

@app.route("/", methods = ["GET"])
def hello():
    return "hello"

# 테스트를위한 주석입니다. 
if __name__ == '__main__':
    app.run( port = 5000)
