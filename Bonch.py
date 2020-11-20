from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://lk.sut.ru/cabinet/?login=no")

browser.find_element_by_name("users").send_keys("lolu4ka@gmail.com")
browser.find_element_by_name("parole").send_keys("orifeh99")

browser.find_element_by_name("logButton").click()

time.sleep(3)

browser.find_element_by_id("heading1").click()
browser.find_element_by_id("menu_li_6118").click()

time.sleep(3)

#browser.find_element_by_link_text("Начать занятие").click()

time.sleep(5)

browser.get("https://lk.sut.ru/cabinet/?login=no")

browser.find_element_by_name("users").send_keys("gnataly2106@mail.ru")
browser.find_element_by_name("parole").send_keys("Andrey2002")

browser.find_element_by_name("logButton").click()

time.sleep(3)

browser.find_element_by_id("heading1").click()
browser.find_element_by_id("menu_li_6118").click()

time.sleep(3)

#browser.find_element_by_link_text("Начать занятие").click()

#print("Препод не ожил к паре(9(\nИли произошла внутренняя ошибка в программе")