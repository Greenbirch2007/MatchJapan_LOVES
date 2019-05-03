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
    driver = webdriver.Firefox()
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
        pyautogui.keyDown("down")  # 下翻页成功！
        time.sleep(6)  # 每三秒往下翻一页
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
        print(big_list)



# #
# create table All_links(
# id int not null primary key auto_increment,
# links text
# ) engine=InnoDB  charset=utf8;

# drop table First_info;


