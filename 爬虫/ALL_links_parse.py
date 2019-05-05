#! -# ! -*- coding:utf-8 -*-

import time
import re
import urllib

import pyautogui
import pymysql
import requests
from selenium import webdriver
# 还是要用PhantomJS
import datetime
import string
from lxml import etree
import random

all_list=[]

    # 使用cursor()方法获取操作游标
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='MatchJ_love',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cur = connection.cursor()
#sql 语句
for i in range(1,13525):
    sql = 'select links from Distinct_links where id = %s ' % i
    # #执行sql语句
    cur.execute(sql)
    # #获取所有记录列表
    data = cur.fetchone()
    url = data['links']
    try:
        if len(url) !=92:
            print("有异常链接")
        else:
            pass
    except:
        pass

