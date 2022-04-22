from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    x = browser.find_element_by_id('num1').text

    y = browser.find_element_by_id('num2').text
    def sum(x, y):
        return str(int(x)+int(y))
    sum = sum(x, y)

    #browser.find_element_by_css_selector("[value='" + y + "']")

    #browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("option:nth-child(2)").click()
    #browser.find_element_by_css_selector("[value='sum']").click()

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)  # ищем элемент с текстом "Python"


    #input1 = browser.find_element_by_id("answer")
    #input1.send_keys(sum)


    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()


finally:
    # успеваем скопировать код за 3 секундs
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

