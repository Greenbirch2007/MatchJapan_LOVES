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

    url = 'https://jp.match.com/login/'   # 直接到登录界面！
    driver = webdriver.Chrome()
    driver.get(url)


    driver.find_element_by_xpath('//*[@id="email"]').send_keys("291109028@qq.com") #用户名
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("mingyifan2007")#密码
    #点击登录
    driver.find_element_by_xpath('//*[@id="mainContent"]/section/form/div/div/div[1]/div[5]/button').click()
    # 点击搜索按钮
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/header/nav/div/ul/li[2]/button/div[1]/div[1]/div/span').click()
    # 下面为一直下拉的脚本
    while True:
        time.sleep(6)  # 每三秒往下翻一页

        pyautogui.keyDown("down")  # 按下往下

        time.sleep(1)  # 要进行测试的参数
        pyautogui.keyUp("down")  # 按下往下



        html = driver.page_source
        selector = etree.HTML(html)
        links = selector.xpath(
            '//*[@id="mainContent"]/section/section/div[2]/div[2]/div/div[1]/div/div/li/div/span/div/a/div/img/@aria-describedby')
        for item in links:
            big_list.append(('https://jp.match.com/profile/'+str(item)+'?page=2&searchType=oneWaySearch&sortBy=1'))

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='MatchJ_love',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.executemany('insert into All_links (links) values (%s)', big_list)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
        print(datetime.datetime.now())



# # #
# create table All_links(
# id int not null primary key auto_increment,
# links text
# ) engine=InnoDB  charset=utf8;
#
# drop table All_links;
#
# create table Distinct_links(
# id int not null primary key auto_increment,
# links text
# ) engine=InnoDB  charset=utf8;
#
# drop table Distinct_links;


#　最终剔除重复项后，有１３５００人！，回头在整理吧


# 剔除重复项后插入新表

# insert into Distinct_links(links) select distinct links from All_links;

# 分年龄段进行筛选，不要一起来！系统不会一次加载全部的＃
# nan--->nv (还是要尽可能细化)
# 18-20 完成20:00
# 21-25 完成20:40
# 26-30 完成　21:16
# 31-35 完成２１：５０
# 36-40　完成22:26
# 41-45 次日０９：４１
# 46-50　次日１０：１６
# 所有



# select count(*) from  All_links;


# 为了测试而用的sql



#
# drop  database MatchJ_love;
# create database MatchJ_love;
# use MatchJ_love;
#
# create table All_links(
# id int not null primary key auto_increment,
# links text
# ) engine=InnoDB  charset=utf8;
#
#
# create table Distinct_links(
# id int not null primary key auto_increment,
# links text
# ) engine=InnoDB  charset=utf8;
