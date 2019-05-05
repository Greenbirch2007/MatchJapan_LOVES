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

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出


def call_pages(url):
    driver.get(url)
    time.sleep(3)
    html = driver.page_source

    return html

# 同一个脚本，把数据和下载图片分开处理
#　优化，做一个判断，如果没有图片，就直接break! 不能傻傻的等着！这样太没有效率了！



def Python_sel_Mysql():
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
        yield url




# 图片下载放弃了，搞点数据吧


# 先登录，再遍历访问路由
if __name__ == '__main__':
    picDown = []

    url = 'https://jp.match.com/login/'  # 直接到登录界面！
    driver = webdriver.Firefox()

    driver.get(url)

    driver.find_element_by_xpath('//*[@id="email"]').send_keys("291109028@qq.com")  # 用户名
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("mingyifan2007")  # 密码
    # 点击登录
    driver.find_element_by_xpath('//*[@id="mainContent"]/section/form/div/div/div[1]/div[5]/button').click()
    time.sleep(1)

    for url_str in Python_sel_Mysql():

        pyautogui.keyDown("down")  # 按下往下
        url_Person = url_str
        html = call_pages(url_str)
        selector = etree.HTML(html)
        # 图像图片
        p_f = []
        # 需要一个不公开数据的情况，需要额外进行判断
        not_open = selector.xpath('//*[@id="mainContent"]/section/h2/span/text()')
        picture1 = selector.xpath('//*[@id="mainContent"]/section/article/div[2]/div[1]/img/@src')
        pictures2 = selector.xpath('//*[@id="mainContent"]/section/article/section[3]/div/div/div/div/div/img/@src')

        #还是要头像的图片的！就放一个晚上
        # 只打印有其他很多图片的头像，只有一个头像就算了


        #如果没有图片，就直接跳过，有了再去添加，遍历  优化测试

        if len(pictures2) == 0:

            print("本页面没有图片～～～～")
            continue  # 必须放在一个循环体中！所以稍微改动一些
            # break是跳过所有循环，continue是跳过本次循环

        elif len(not_open)==9:
            print("本页面没有图片～～～～")
            continue  # 必须放在一个循环体中！所以稍微改动一些
            # break是跳过所有循环，continue是跳过本次循环


        else:
            for i in picture1:
                p_f.append(i)

            for i in pictures2:
                p_f.append(i)

            for item in p_f:
                downPic = item[:-11]
                picDown.append(downPic)

            try:
                for item in picDown:
                    url_name = url_Person[29:52] + random.choice(url_Person)


                    urllib.request.urlretrieve(item, '/home/g/Documents/matchLove_Pics/%s.jpg' % url_name )
                    print(datetime.datetime.now())
            except:
                pass

