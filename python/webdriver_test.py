"""
Webdriver test using pytest module (CentOS 7)

To run test:
- install latest Selenium version
    > pip install -U selenium
- install latest Firefox browser
    > yum install firefox
- get latest geckodriver
    https://github.com/mozilla/geckodriver/releases
- install pytest
    > yum install pytest

Execute:
# py.test webdriver_test.py

GIT

mkdir /root/python/practice
cd /root/python/practice
git clone https://github.com/belgeu/misc.git
cd misc
## edit .git/config to ask pass (add belgeu@ to url)
## url = https://belgeu@github.com/belgeu/misc.git
git add webdriver_test.py
git commit -m "Initial revision of webdriver test"
git push origin master

"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser(request):
    driver = webdriver.Firefox()
    def teardown():
        driver.quit()
    request.addfinalizer(teardown)
    return driver

def test_01(browser):
    b = browser
    b.get("https://docs.python.org/")
    e = b.find_element_by_link_text('Tutorial')
    e.click()
    element = WebDriverWait(b, 10).until(
        EC.presence_of_element_located((By.ID, "the-python-tutorial"))
    )
