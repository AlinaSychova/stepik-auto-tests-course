from selenium import webdriver
import time 
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    #sleep(10)
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@test.com")

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    option1 = browser.find_element_by_name("file")
    #print(os.path.abspath("/Users/alinasychova/selenium_course"))
    print(option1)
    #option1.click()
    current_dir = os.path.abspath(os.path.dirname("/Users/alinasychova/selenium_course/"))
    print(current_dir)
    file_path = os.path.join(current_dir, 'New.txt') 
    print(file_path)
    option1.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

