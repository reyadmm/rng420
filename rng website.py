from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get('https://www.random.org/integers/')
driver.find_element_by_name('num').send_keys(chr(127)*3 + '1')
driver.find_element_by_name('min').send_keys(chr(127)*3 + '69')
driver.find_element_by_name('max').send_keys(chr(127)*3 + '666')
driver.find_element_by_name('col').send_keys(chr(127)*3 + '1')
time.sleep(1)
driver.find_element_by_xpath("//input[@value='Get Numbers']").click()
number = driver.find_element_by_class_name('data').text
while not number.startswith('420'):
    driver.find_element_by_xpath("//input[@value='Again!']").click()
    number = driver.find_element_by_class_name('data').text
