from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

link = "http://suninjuly.github.io/alert_accept.html"
wd = webdriver.Chrome()
wd.get(link)

wd.find_element_by_tag_name("button").click()
confirm = wd.switch_to.alert.accept()
x = int(wd.find_element_by_css_selector("span#input_value").text)
res = calc(x)
wd.find_element_by_id("answer").send_keys(res)
wd.find_element_by_tag_name("button").click()
alert_text = wd.switch_to.alert.text
print(alert_text.split(': ')[-1])
wd.quit()