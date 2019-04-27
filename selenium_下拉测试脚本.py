#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

if __name__ == '__main__':
    url = "http://blog.csdn.net/"

    browser = webdriver.Chrome()
    browser.get(url)

    browser.execute_script("""
    (function () {
    var y = 0;
    var step = 100;
    window.scroll(0, 0);
    function f() {
    if (y < document.body.scrollHeight) {
    y += step;
    window.scroll(0, y);
    setTimeout(f, 100);
    } else {
    window.scroll(0, 0);
    document.title += "scroll-done";
    }
    }
    setTimeout(f, 1000);
    })();
    """)
    print("下拉中...")
    # time.sleep(180)
    while True:
        if "scroll-done" in browser.title:
            break
    else:
        print("还没有拉到最底端...")
        time.sleep(3)