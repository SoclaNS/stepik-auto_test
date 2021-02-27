import time
from math import log, sin
from selenium import webdriver


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn").click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    redirect = browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector(".nowrap#input_value").text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()
