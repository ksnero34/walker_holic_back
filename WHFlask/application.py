#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import ssl
import requests
# import sql_connect

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #



@app.route("/walk_data", methods = ['GET'])
def admin_to_login2():
    data = {'name' : '한준규', 'test':'test입니다.'}
    return jsonify(data)



@app.route("/input", methods = ['GET','POST'])
def admin_to_login():
    parm = request.get_json()
    return parm['type']

@app.route("/민원내용", methods = ['GET'])
def admin_to_login3():
    return "민원내용을 json형슥으로 받아 db에 넣습니다."

if __name__ == '__main__':
    app.run( port = 5000 )
