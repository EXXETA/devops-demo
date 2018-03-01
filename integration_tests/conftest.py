import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def chrome():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--single-process')

    try:
        driver = webdriver.Chrome(
            os.environ['CHROME_DRIVER_PATH'],
            options=chrome_options
        )
    except KeyError:
        driver = webdriver.Chrome(
            options=chrome_options
        )

    return driver
