from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/get_attribute.html"
wd = webdriver.Chrome()
wd.get(link)

x = int(wd.find_element_by_css_selector("img#treasure").get_attribute("valuex"))
res = calc(x)
wd.find_element_by_id("answer").send_keys(res)
wd.find_element_by_id("robotCheckbox").click()

human_checked = wd.find_element_by_id("humanRule").get_attribute("checked")
print("Value of human radio: ", human_checked)
assert human_checked is not None, "Human radio is not selected by default"

wd.find_element_by_id("robotsRule").click()
wd.find_element_by_css_selector(".btn.btn-default").click()
