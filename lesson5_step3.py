from selenium import webdriver
import math

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

#link_part = str(math.ceil(math.pow(math.pi, math.e)*10000))

#wd.find_element_by_partial_link_text(link_part).click()

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()