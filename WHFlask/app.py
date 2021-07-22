#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import ssl
import requests
# import sql_connect

application = Flask(__name__)
application.config['JSON_AS_ASCII'] = False #



@application.route("/walk_data", methods = ['GET'])
def admin_to_login2():
    data = {'name' : '한준규', 'test':'test입니다.'}
    return jsonify(data)

@application.route("/input", methods = ['GET','POST'])
def admin_to_login():
    parm = request.get_json()
    return "json_data.를 받아왔습니다.",parm

@application.route("/민원내용", methods = ['GET'])
def admin_to_login3():
    return "민원내용을 json형슥으로 받아 db에 넣습니다."

if __name__ == '__main__':
    application.run('0.0.0.0', port = 80, debug = True)
