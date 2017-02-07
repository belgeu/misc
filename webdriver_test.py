"""
Webdriver test

To run test:
- install latest Selenium version
    pip install -U selenium
- install latest Firefox browser
- get latest geckodriver
    https://github.com/mozilla/geckodriver/releases

Execute:
# python webdriver_test.py


GIT

mkdir /root/python/practice
cd /root/python/practice
git init
git add webdriver_test.py
git commit -m "Initial revision of webdriver test"
git push

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
b = webdriver.Firefox()
b.get("https://docs.python.org/")
e = b.find_element_by_link_text('Tutorial')
e.click()

try:
    element = WebDriverWait(b, 10).until(
        EC.presence_of_element_located((By.ID, "the-python-tutorial"))
    )
finally:
    b.quit()
