from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


def math_task(wd):
    x = int(wd.find_element_by_css_selector("span#input_value").text)
    res = calc(x)
    wd.find_element_by_id("answer").send_keys(res)
    wd.find_element_by_id("solve").click()
    alert_text = wd.switch_to.alert.text
    print(alert_text.split(': ')[-1])


link = "http://suninjuly.github.io/explicit_wait2.html"
wd = webdriver.Chrome()
wd.get(link)

wait = WebDriverWait(wd, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
wd.find_element_by_css_selector("button#book").click()

math_task(wd)

wd.quit()