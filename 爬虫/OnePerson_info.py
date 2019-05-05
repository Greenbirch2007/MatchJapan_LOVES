#! -# ! -*- coding:utf-8 -*-

import time
import re
import urllib

import pymysql
import requests
from selenium import webdriver
# 还是要用PhantomJS
import datetime
import string
from lxml import etree
import random



def call_pages(url):
    driver.get(url)
    time.sleep(3)
    html = driver.page_source

    return html


def parse_pages(html):
    big_list = []
    selector = etree.HTML(html)
    name = selector.xpath('//*[@id="mainContent"]/section/article/div[2]/div[2]/div[1]/div[1]/h2/div/text()')
    age_location = selector.xpath('//*[@id="mainContent"]/section/article/div[2]/div[2]/div[2]/span/text()')
    couple_g = selector.xpath('//*[@id="mainContent"]/section/article/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/text()')
    education = selector.xpath('//*[@id="mainContent"]/section/article/section[2]/div/ul/li[2]/div[1]/div/span/text()')
    high = selector.xpath('//*[@id="mainContent"]/section/article/section[2]/div/ul/li[8]/div[1]/div/span/text()')
    rearch_for = selector.xpath('//*[@id="mainContent"]/section/article/div[2]/div[2]/div[3]/span/span/text()')
    pictures = selector.xpath('//*[@id="mainContent"]/section/article/section[3]/div/div/div/div/div/img/@src')
    for item in pictures:
        downPic = item[:-11]
        picDown.append(downPic)



    for i1,i2,i3,i4,i5,i6 in zip(name,age_location,couple_g,education,high,rearch_for):
        big_list.append((i1,i2,i3,i4,i5,i6))

    return big_list


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





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='MatchJ_love',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into MatchLove_OnePersonInfo (name,age_location,couple_g,education,high,rearch_for) values (%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except Exception :
        print('出列啦')






# 先登录，再遍历访问路由
if __name__ == '__main__':
    picDown = []

    url = 'https://jp.match.com/login/'  # 直接到登录界面！
    driver = webdriver.Chrome()
    driver.get(url)

    driver.find_element_by_xpath('//*[@id="email"]').send_keys("291109028@qq.com")  # 用户名
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("mingyifan2007")  # 密码
    # 点击登录
    driver.find_element_by_xpath('//*[@id="mainContent"]/section/form/div/div/div[1]/div[5]/button').click()
    time.sleep(1)


    for url_str in Python_sel_Mysql():
        url_Person = url_str
        html = call_pages(url_Person)
        content = parse_pages(html)
        insertDB(content)

        for item in picDown:
            url_name = url_Person[29:52] + random.choice(url_Person)

            urllib.request.urlretrieve(item, '/home/g/Documents/matchLove_Pics/%s.jpg' % url_name )

        print(datetime.datetime.now())









# create table MatchLove_OnePersonInfo (
# id int not null primary key auto_increment,
# name varchar(30),
# age_location varchar(60),
# couple_g varchar(30),
# education varchar(30),
# high varchar(30),
# rearch_for text
# ) engine =InnoDB charset=utf8;

# drop table MatchLove_OnePersonInfo;
#


