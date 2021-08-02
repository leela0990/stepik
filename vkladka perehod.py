import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('body > form > div > div > button')
    button1.click()

    new_win = browser.window_handles[1]
    browser.switch_to.window(new_win)

    x1 = browser.find_element_by_id("input_value")
    x = x1.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    button2 = browser.find_element_by_css_selector("body > form > div > div > button")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла