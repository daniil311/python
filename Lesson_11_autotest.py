from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id('treasure')
    x = (x_element.get_attribute("valuex"))
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()


finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(9)
    # закрываем браузер после всех манипуляций
    browser.quit()

