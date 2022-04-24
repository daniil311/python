from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='firstname']")
    input1.send_keys("Henry")
    input2 = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='lastname']")
    input2.send_keys("Ford")
    input3 = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='email']")
    input3.send_keys("test@mail.ru")

    current_dir = os.path.abspath(os.path.dirname('__file__'))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    #element.send_keys(file_path)

    input4 = browser.find_element_by_xpath('//input[@type="file"]')
    #input4 = browser.find_element_by_id('file')
    input4.send_keys(file_path)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
