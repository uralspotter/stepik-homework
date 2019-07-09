from selenium import webdriver
import time


def my_test(link):
    wd = webdriver.Chrome()
    wd.get(link)

    wd.find_element_by_xpath("//div[contains(@class, 'first_block')]//input[contains(@class, 'first')]").send_keys(
        "Name")
    wd.find_element_by_xpath("//div[contains(@class, 'first_block')]//input[contains(@class, 'second')]").send_keys(
        "Family")
    wd.find_element_by_xpath("//div[contains(@class, 'first_block')]//input[contains(@class, 'third')]").send_keys(
        "mail@mail.mail")

    wd.find_element_by_tag_name("button").click()
    time.sleep(1)

    welcome_text = wd.find_element_by_tag_name("h1").text

    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
    wd.quit()


link_form1 = "http://suninjuly.github.io/registration1.html"
link_form2 = "http://suninjuly.github.io/registration2.html"

my_test(link_form1)
my_test(link_form2)
