from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#Посчитать математическую функцию от x (сама функция остаётся неизменной).

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))


# Взять у этого элемента (картинки) значение атрибута valuex, которое является значением x для задачи   
    treasure = browser.find_element_by_id("treasure")
    x_element = treasure.get_attribute("valuex")
    x = x_element
    y = calc(x)

#Ввести ответ в текстовое поле

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

# Отметить checkbox "I'm the robot".

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

#Выбрать radiobutton "Robots rule!".

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

#Нажать на кнопку "Submit".

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

# ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()   

