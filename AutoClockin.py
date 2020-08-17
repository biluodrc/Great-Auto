# -*- coding = utf-8 -*-
# @time: 2020/8/17 20:45
# Author: Biluo
# @File: AutoClockin.py

from selenium import webdriver
from time import sleep

username = 'username'
password = 'password'

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
submitB = broswer.find_elements_by_class_name('command_button_content')
submitB[0].click()
sleep(3)
temB = broswer.find_element_by_class_name('dialog_footer')
okB = temB.find_element_by_tag_name('button')
okB.click()
