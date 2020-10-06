from selenium import webdriver
import time 
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

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

    #Отметить checkbox "I'm the robot".
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    

    #Проскроллить страницу вниз. Выбрать radiobutton "Robots rule!". 
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    

    #Проскроллить страницу вниз. Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


