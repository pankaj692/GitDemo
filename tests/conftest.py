import pytest
from selenium import webdriver
import time



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # driver = webdriver.Chrome(executable_path="C:\\Python\\Python39\\chromedriver.exe")
        driver = webdriver.Chrome()
        driver.get("https://www.sbmailer.com/")
        driver.maximize_window()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.get("https://www.sbmailer.com/")
        driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()





