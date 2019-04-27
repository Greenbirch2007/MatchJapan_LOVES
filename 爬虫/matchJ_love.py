#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import pyautogui



# 把find_elements 改为　find_element
# def get_first_page(url):


    # driver.find_element_by_xpath('//*[@id="topIndex"]/div/p/a[2]').click()
    # driver.find_element_by_xpath('//*[@id="kwdselectid"]').send_keys("赴日")  #可以针对其他岗位进行统计分析
    # # 还要剔除本地选项　　（“”）
    # driver.find_element_by_xpath('//*[@id="work_position_input"]').click()
    # driver.find_element_by_xpath('//*[@id="work_position_click_multiple_selected_each_200200"]').click()
    # driver.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()
    # driver.find_element_by_xpath('/html/body/div[2]/form/div/div[1]/button').click()
    # html = driver.page_source
    # return html





# 把首页和翻页处理？

def next_page():
    for i in range(1,32):  # selenium 循环翻页成功！
        driver.find_element_by_xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[last()]/a').click()
        time.sleep(1)
        html = driver.page_source
        return html



def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    big_list = []
    selector = etree.HTML(html)
    jobs = selector.xpath("//div[@class='dw_table']/div/p/span[1]/a/@title")
    link = selector.xpath("//div[@class='dw_table']/div/p/span[1]/a/@href")
    firms = selector.xpath('//*[@id="resultList"]/div/span[1]/a/text()')
    long_tuple = (i for i in zip(jobs, link, firms))
    for i in long_tuple:
        big_list.append(i)
    return big_list


        # 存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='JOB',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into GoTo_j1 (jobs,link,firms) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass





if __name__ == '__main__':
    url = 'https://jp.match.com/login/'   # 直接到登录界面！
    driver = webdriver.Firefox()
    driver.get(url)
    # print("开始访问")
    # driver.find_element_by_xpath('//*[@id="pageBody"]/div[2]/div/p/a').click()
    # print("到搜索界面")

    driver.find_element_by_xpath('//*[@id="email"]').send_keys("291109028@qq.com") #用户名
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("mingyifan2007")#密码
    #点击登录
    driver.find_element_by_xpath('//*[@id="mainContent"]/section/form/div/div/div[1]/div[5]/button').click()
    # 点击搜索按钮
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/header/nav/div/ul/li[2]/button/div[1]/div[1]/div/span').click()
    # 下面为一直下拉的脚本
    while True:

        time.sleep(10)  # 每三秒往下翻一页
        pyautogui.keyDown("down")  # 下翻页成功！
        time.sleep(10)  # 每三秒往下翻一页
        html = driver.page_source
        print(html)

        # driver.find_element_by_id('kw').send_keys(Keys.PAGE_DOWN)


    # time.sleep(180)
    # while True:
    #
    #     if "scroll-done" in driver.title:
    #
    #         break
    #
    #     else:
    #         print("还没有拉到最底端...")
    #         time.sleep(3)


    # html = get_first_page()
    # content = parse_html(html)
    # time.sleep(1)
    # insertDB(content)
    # while True:
    #     html = next_page()
    #     content = parse_html(html)
    #     insertDB(content)
    #     print(datetime.datetime.now())
    #     time.sleep(1)


# #
# create table GoTo_j1(
# id int not null primary key auto_increment,
# jobs varchar(80),
# link varchar(88),
# firms varchar(80)
# ) engine=InnoDB  charset=utf8;



