from selenium.webdriver.support.ui import Select
from selenium import webdriver

link = "http://suninjuly.github.io/selects2.html"
wd = webdriver.Chrome()
wd.get(link)

x = int(wd.find_element_by_id("num1").text)
y = int(wd.find_element_by_id("num2").text)
z = str(x+y)
select = Select(wd.find_element_by_tag_name("select"))
select.select_by_value(z)
wd.find_element_by_css_selector("button[type='submit']").click()