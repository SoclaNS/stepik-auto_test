import time
from math import log, sin
from selenium import webdriver


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    """unique_selectors = [
        'input.form-control[name="firstname"]',   # First name
        'input.form-control[name="lastname"]',  # Last name
        'input.form-control[name="email"]',   # Email
    ]
    for selector in unique_selectors:
        element = browser.find_element_by_css_selector(selector)
        element.send_keys("Ответ")"""

    button = browser.find_element_by_css_selector("button.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_css_selector(".nowrap#input_value").text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()
