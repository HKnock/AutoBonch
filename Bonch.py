from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os

print("Программа начинает балдеть")

now = datetime.datetime.now()
hour = now.hour
minute = now.minute
current_time = hour * 60 + minute + 180
nowa_day = datetime.date.today().weekday() 

try:
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    browser = webdriver.Chrome()
    browser.get("https://lk.sut.ru/cabinet/?login=no")

    print("Программа берёт аДский разгон на балдёж")

# Первый пользователь
    try:
        if(
        ((current_time >= 540 and current_time <= 635) or
        (current_time >= 645 and current_time <= 740) or
        (current_time >= 780 and current_time <= 875) or
        (current_time >= 885 and current_time <= 980) or
        (current_time >= 990 and current_time <= 1085) or
        (current_time >= 1095 and current_time <= 1190) or 
        (current_time >= 1200 and current_time <= 1295)) 
        and nowa_day != 6
        ):
            print("Программа балдеет за первого пользователя")

            browser.find_element_by_name("users").send_keys("lolu4ka@gmail.com")
            browser.find_element_by_name("parole").send_keys("orifeh99")

            browser.find_element_by_name("logButton").click()

            time.sleep(3)

            browser.find_element_by_id("heading1").click()
            browser.find_element_by_id("menu_li_6118").click()

            time.sleep(3)

            browser.find_element_by_link_text("Начать занятие").click()

            time.sleep(5)
    except:
        print("Пользователь сломал систему(9(\nПрограмма не балдеет")

# Второй пользователь
    try:
        if(
        ((current_time >= 540 and current_time <= 635) or
        (current_time >= 645 and current_time <= 740) or
        (current_time >= 780 and current_time <= 875) or
        (current_time >= 885 and current_time <= 980) or
        (current_time >= 990 and current_time <= 1085) or
        (current_time >= 1095 and current_time <= 1190) or 
        (current_time >= 1200 and current_time <= 1295)) 
        and nowa_day != 6
        ):
            print("Программа балдеет за второго пользователя")

            browser.get("https://lk.sut.ru/cabinet/?login=no")

            browser.find_element_by_name("users").send_keys("gnataly2106@mail.ru")
            browser.find_element_by_name("parole").send_keys("Andrey2002")

            browser.find_element_by_name("logButton").click()

            time.sleep(3)

            browser.find_element_by_id("heading1").click()
            browser.find_element_by_id("menu_li_6118").click()

            time.sleep(3)

            browser.find_element_by_link_text("Начать занятие").click()

            time.sleep(5)
    except:
        print("Пользователь сломал систему(9(\nПрограмма не балдеет")

# Третий пользователь
    try:
        if(
        ((current_time >= 540 and current_time <= 635) or
        (current_time >= 645 and current_time <= 740) or
        (current_time >= 780 and current_time <= 875) or
        (current_time >= 885 and current_time <= 980) or
        (current_time >= 990 and current_time <= 1085) or
        (current_time >= 1095 and current_time <= 1190) or 
        (current_time >= 1200 and current_time <= 1295)) 
        and nowa_day != 6
        ):
            print("Программа балдеет за третьего пользователя")

            browser.get("https://lk.sut.ru/cabinet/?login=no")

            browser.find_element_by_name("users").send_keys("ivanoov16@mail.ru")
            browser.find_element_by_name("parole").send_keys("novgorod03")

            browser.find_element_by_name("logButton").click()

            time.sleep(3)

            browser.find_element_by_id("heading1").click()
            browser.find_element_by_id("menu_li_6118").click()

            time.sleep(3)

            browser.find_element_by_link_text("Начать занятие").click()

            time.sleep(3)
    except:
        print("Пользователь сломал систему(9(\nПрограмма не балдеет")

# Четвёртый пользователь
    try:
        if(
        ((current_time >= 540 and current_time <= 635) or
        (current_time >= 645 and current_time <= 740) or
        (current_time >= 780 and current_time <= 875) or
        (current_time >= 885 and current_time <= 980) or
        (current_time >= 990 and current_time <= 1085) or
        (current_time >= 1095 and current_time <= 1190) or 
        (current_time >= 1200 and current_time <= 1295)) 
        and nowa_day != 6
        ):
            print("Программа балдеет за четвёртого пользователя")

            browser.get("https://lk.sut.ru/cabinet/?login=no")

            browser.find_element_by_name("users").send_keys("lyagiceva@mail.ru")
            browser.find_element_by_name("parole").send_keys("Kirik5218")

            browser.find_element_by_name("logButton").click()

            time.sleep(3)

            browser.find_element_by_id("heading1").click()
            browser.find_element_by_id("menu_li_6118").click()

            time.sleep(3)

            browser.find_element_by_link_text("Начать занятие").click()

    except:
        print("Пользователь сломал систему(9(\nПрограмма не балдеет")

except:
    print("Препод не ожил к паре(9(\nИли произошла внутренняя ошибка в программе\nПрограмма не балдеет(9(")
