from selenium import webdriver
import time 
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки alert
    time.sleep(1)

    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()


    # ждем загрузки страницы
    time.sleep(3)


    #Посчитать математическую функцию от x
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    #Считать значение для переменной x.
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    #Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


