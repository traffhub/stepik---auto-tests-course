from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "C:\chromedriver\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

browser.get('http://suninjuly.github.io/math.html')

people_radio=browser.find_element_by_id('peopleRule')
people_checked=people_radio.get_attribute('checked')
print('value of people radio: ',people_checked)
assert people_checked is not None, "People radio is not selected by default"

Robots_radio = browser.find_element_by_id('robotsRule')
Robots_checked = Robots_radio.get_attribute('checked')
assert Robots_checked is None, 'suka blya'

button = browser.find_element_by_css_selector('.btn.btn-default')
button_disabled = button.get_attribute('disabled')
print('no button: ',button_disabled)
assert button_disabled is None, 'кнопка есть'

time.sleep(10)
button_disabled = button.get_attribute('disabled')
print('no button: ',button_disabled)
assert button_disabled is not None, 'кнопки нет'
