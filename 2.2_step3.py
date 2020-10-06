from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


#Посчитать сумму заданных чисел

    def calc(z):
      return str(int(x)+int(y))

    x_element = browser.find_element_by_id("num1")
    x = x_element.text

    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    z = calc(x+y)  

#Выбрать в выпадающем списке значение равное расчитанной сумме

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    

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
