#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import pyautogui



if __name__ == '__main__':
    big_list = []

    url = 'https://www.cnblogs.com/dcb3688/p/4607980.html'   # 直接到登录界面！
    driver = webdriver.Chrome()
    driver.get(url)


    while True:

        pyautogui.keyDown("down")  # 按下往下

        time.sleep(0.05)  # 每三秒往下翻一页
        pyautogui.keyUp("down")  # 按下往下






