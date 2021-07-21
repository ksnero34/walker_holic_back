#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, request, render_template, jsonify
import ssl
import requests
# import sql_connect

application = Flask(__name__)
application.config['JSON_AS_ASCII'] = False


@application.route("/walk_data", methods = ['GET'])
def admin_to_login2():
    return "요청이 들어오면 db에서 공지사항 내용을 json 형식으로 웹에 보여줍니다."

@application.route("/input", methods = ['GET'])
def admin_to_login():
    return "산책데이터를 json으로 받아 db에 넣습니다."

@application.route("/민원내용", methods = ['GET'])
def admin_to_login3():
    return "민원내용을 json형슥으로 받아 db에 넣습니다."

if __name__ == '__main__':
    application.run('0.0.0.0', port = 80, debug = True)
