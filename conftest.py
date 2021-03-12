import pytest
from selenium import webdriver

executable_path = {'executable_path': r'.\Drivers\chromedriver'}


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="choose your browser")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(**executable_path)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{browser} is not supported!")

    driver.implicitly_wait(5)
    driver.maximize_window()
    # request.addfinalizer(driver.quit)

    return driver
