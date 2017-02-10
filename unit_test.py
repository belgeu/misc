import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class UnitTest(unittest.TestCase):
 
    def setUp(self):
        self.b = webdriver.Firefox()
 
    def test_1(self):
        b = self.b
        b.get("https://docs.python.org/")
        e = b.find_element_by_link_text('Tutorial')
        e.click()
        element = WebDriverWait(b, 10).until(
            EC.presence_of_element_located((By.ID, "the-python-tutorial"))
        )

    def tearDown(self):
        self.b.close()

 
if __name__ == '__main__':
    unittest.main()