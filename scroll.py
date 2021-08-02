import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://SunInJuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("#input_value")

    def calc(x):
        return ln(abs(12 * sin(x)))
    y=calc(x)

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollintoview(true);" button)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла