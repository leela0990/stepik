from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(2)')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(4)')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(6)')
    input3.send_keys("test@ya.ru")


    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого скрипта
    file_name = "try.txt" # имя файла, который будем загружать на сайт
    file_path = os.path.join(current_dir, file_name) # получаем путь к file_name
    element = browser.find_element_by_id('file') # находим элемент для загрузки
    element.send_keys(file_path) # отправляем файл

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла