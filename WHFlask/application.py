#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import ssl
import requests
from controller import json_handler
# import sql_connect

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #



@app.route("/walk_data", methods = ['GET'])
def admin_to_login2():
    data =[ {'id': 1 ,'title':'멸종', 'url' : '대머리'},
	     {'id' : 2, 'title': '이선우', 'url' : 'ㅋㅋ'}]
    return jsonify(data)

@app.route("/input", methods = ['GET','POST'])
def admin_to_login():
    print("123123123")
    parm = request.get_json()
    json_handler.input_json_data(parm)
    print(parm['type'])
    return parm['type']


@app.route("/", methods = ["GET"])
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(port = 5000, Debug=True)
