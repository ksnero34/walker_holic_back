#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import ssl
import requests
from controller import json_handler
# import sql_connect
import sys
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #


@app.route("/walk_data", methods = ['GET'])
def admin_to_login2():
    data =[ {'id': 1 ,'title':'멸종', 'url' : '대머리'},
	     {'id' : 2, 'title': '이선우', 'url' : 'ㅋㅋ'}]
    return jsonify(data)

@app.route("/input", methods = ['GET','POST'])
def admin_to_login():
    type = request.form["type"]
    title = request.form["title"]
    # file_img = request.files['image']
    # file_img.save(secure_filename(file_img.filename))


    # f = open("test.txt", "wr")
    # f.write(type)
    # f.close()
    return 1


@app.route("/", methods = ["GET"])
def hello():
    return "hello"
# 테스트를위한 주석입니다. 
if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000)
