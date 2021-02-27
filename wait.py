import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.card-body #price'), '$100')
    )
    browser.find_element_by_css_selector("#book.btn-primary").click()

    """button = browser.find_element_by_css_selector("button.btn").click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    redirect = browser.switch_to.window(new_window)"""

    x = browser.find_element_by_css_selector(".nowrap#input_value").text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn-primary#solve").click()

finally:
    time.sleep(5)
    browser.quit()
