'''
instruction：登录 163 邮箱示例
author：程序员野客
'''

# 需先将二维码登录方式切换到用户名密码登录方式
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(2)
browser.get('https://mail.163.com/')
# 将扫码登录转切换为用户名密码登录
browser.find_element_by_xpath('//div[@id="lbNormal"]').click()
# 转化登录方式之后，要进入iframe框
browser.switch_to.frame(browser.find_element_by_xpath('//iframe[starts-with(@id,"x-URS")]'))
# 自己的用户名
browser.find_element_by_xpath('//input[@name="email"]').send_keys('xxx')
# 自己的密码
browser.find_element_by_xpath('//input[@name="password"]').send_keys('xxx')
browser.find_element_by_xpath('//*[@id="dologin"]').click()
print(browser.page_source)
browser.quit()
