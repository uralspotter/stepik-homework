from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

wd = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
wd.get(link)

x = int(wd.find_element_by_css_selector("span#input_value").text)
res = calc(x)
wd.find_element_by_id("answer").send_keys(res)
button = wd.find_element_by_tag_name("button")
wd.execute_script("return arguments[0].scrollIntoView(true);", button)
wd.find_element_by_id("robotCheckbox").click()

wd.find_element_by_id("robotsRule").click()

button.click()
assert True