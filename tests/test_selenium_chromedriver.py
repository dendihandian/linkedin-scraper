from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")
page_source = driver.page_source
driver.close()

def test_selenium():
    assert "Welcome to Python.org" in page_source