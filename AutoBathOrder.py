# -*- coding = utf-8 -*-
# @time: 2020/8/11 10:03
# Author: Biluo
# @File: AutoBathOrder.py

from selenium import webdriver
import re
import threading
from time import sleep

# 相关信息
# name: 姓名
# phnumber: 手机号
# id: 学号
# sex: 0表示女生 1表示男生
name = '邓若琛'
phnumber = '17808073264'
id = '55180432'
sex = 1

# 所有时间的优先序列，共十三个选择 [1,13]
# 1/  11:00-11:45
# 2/  11:45-12:30
# 3/  12:30-13:15
# 4/  13:15-14:00
# 5/  14:00-14:45
# 6/  14:45-15:30
# 7/  15:30-16:15
# 8/  16:15-17:00
# 9/  17:00-17:45
# 10/ 18:00-18:45
# 11/ 18:45-19:30
# 12/ 19:30-20:15
# 13/ 20:15-21:00
timeidxs = [13 , 2 , 10 , 1 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 11 , 12]

class YuYueThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        print ("开始线程：" + str(self.threadID))
        yuyueFunc()
        print ("退出线程：" + str(self.threadID))

def yuyueFunc():
    pattern = re.compile('^\d{2}:\d{2}-\d{2}:\d{2}\(余：(\d{1,3})\)$')
    broswer = webdriver.Chrome()
    broswer.get('http://hqserver.jlu.edu.cn/yuci.php?xy=addxiyu2&id=8')
    a = broswer.find_element_by_css_selector('tbody tr td a')
    a.click()
    choosetimeA = broswer.find_elements_by_css_selector('tbody tr')
    # 遍历所有预约时间，并判断是否有余量
    for i in range(0 , len(timeidxs)):
        maleA = choosetimeA[timeidxs[i]+1].find_element_by_css_selector('td a')
        text = maleA.text
        remainNum = int(re.match(pattern, text).group(1))
        if (remainNum > 0):
            maleA.click()
            # 填写方框中的信息
            input = broswer.find_elements_by_css_selector('tbody tr td input')
            input[0].send_keys(name)
            input[1].send_keys(phnumber)
            input[2].send_keys(id)

            # 选择性别
            sexB = broswer.find_elements_by_css_selector('tbody tr td label input')
            sexB[sex].click()

            # 提交信息
            submitB = broswer.find_element_by_id('Submit')
            submitB.click()

            # 点击警告弹窗
            alert = broswer.switch_to.alert
            alert_text = alert.text
            if alert_text == '不要重复预约！':
                break
            else:
                alert.accept()

def main():
    # 创建预约线程
    thread1 = YuYueThread(1)
    thread2 = YuYueThread(2)

    # 开启预约线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print ("退出主线程")

if __name__ == '__main__':
    main()
