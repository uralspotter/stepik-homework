from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
wd = webdriver.Chrome()
wd.get(link)

wd.find_element_by_name("firstname").send_keys("Test")
wd.find_element_by_name("lastname").send_keys("Test")
wd.find_element_by_name("email").send_keys("Mail")
wd.find_element_by_id("file").send_keys("C:\\Users\\ural\\environments\\test.txt")
wd.find_element_by_css_selector(".btn.btn-primary").click()