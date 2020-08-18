# -*- coding = utf-8 -*-
# @time: 2020/8/17 20:45
# Author: Biluo
# @File: AutoClockin.py

from selenium import webdriver
from time import sleep
import datetime

username = 'dengrc5518'
password = 'drc991102'

broswer = webdriver.Chrome()
broswer.get('https://ehall.jlu.edu.cn/infoplus/form/BKSMRDK/start')

# login
usernameB = broswer.find_element_by_id('username')
passwordB = broswer.find_element_by_id('password')
loginB = broswer.find_element_by_id('login-submit')
usernameB.send_keys(username)
passwordB.send_keys(password)
loginB.click()
sleep(3)

# clock in
# 选择校区
options = broswer.find_elements_by_tag_name('option')
for i in range(len(options)):
    if (options[i].text == '-请选择-'):
        options[i].click()
    if (options[i].text == '中心校区'):
        options[i].click()
        break
# 选择寝室位置
options = broswer.find_elements_by_tag_name('option')
for i in range(len(options)):
    if (options[i].text == '-请选择-'):
        options[i].click()
    if (options[i].text == '北苑1公寓'):
        options[i].click()
        break
# 输入寝室号
qsI = broswer.find_element_by_name('fieldSQqsh')
qsI.send_keys('2076')

hour = int(datetime.datetime.now().strftime('%H'))
labels = broswer.find_elements_by_tag_name('label')
if (hour == 7):
    for label in labels:
        if (label.text == '正常'):
            label.click()
if (hour == 11):
    for label in labels:
        if (label.text == '正常'):
            label.click()
if (hour == 17):
    for label in labels:
        if (label.text == '正常'):
            label.click()
# 提交
submitB = broswer.find_elements_by_class_name('command_button_content')
submitB[0].click()
sleep(3)
temB = broswer.find_element_by_class_name('dialog_footer')
okB = temB.find_element_by_tag_name('button')
okB.click()
