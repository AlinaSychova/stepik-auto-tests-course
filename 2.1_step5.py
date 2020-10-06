from selenium import webdriver
import time 
import math

try: 
    link = "http://suninjuly.github.io/math.html"
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
    

    #Выбрать radiobutton "Robots rule!".
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    

    #Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


