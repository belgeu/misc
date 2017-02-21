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
    browser.get("https://docs.python.org/")
    element = browser.find_element_by_link_text('Tutorial')
    element.click()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "the-python-tutorial"))
    )
