#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：selenium_so.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/23
#   语言：Python 2.7.x
#   操作：python selenuium.py
#   功能：结合crontab定时启动每天自动登录so网站,刷银牌用
#-------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

#加载内核
driver = webdriver.Chrome()
#driver = webdriver.Chrome()

#发起请求
print 'beging_0'
driver.get("http://lbsyun.baidu.com/skins/MySkin/resources/iframs/heightAccApi.html")
# http://lbsyun.baidu.com/index.php?title=webapi/high-acc-ip

#获取用户名框并输入
print 'beging_1'
elem = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[2]/input')

elem.send_keys("171.15.132.58")

#获取密码框并输入
print 'beging_2'
elem = driver.find_element_by_xpath('//*[@id="HeightMapBtn"]').click()
#elem.send_keys("**")

#通过回车键进行登录
print 'beging_3'
#elem.send_keys(Keys.RETURN)

time.sleep(5)

#保存页面截图和源码
name = './so_img/'+time.ctime().replace(' ','-')+'.png'
#name_html = "./so_img/"+time.ctime().replace(' ','-')+'.html'

driver.save_screenshot(name)
#f = open(name_html.encode('utf-8'),'w')
#f.write(driver.page_source)
#f.close()

print driver.page_source

time.sleep(5)

#driver.quit()
#elem.clear()
#time.sleep(10)
driver.close()
