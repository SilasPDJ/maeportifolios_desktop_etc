import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from time import sleep

from pandas_utilities import *


data = final()


def _driver(path=''):
    """
    :param path: default path atual
    :return: o driver para fechar no loop
    """

    link = "Chromedriver/chromedriver.exe"
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    # profile chrome_options.add_argument("user-data-dir=C:\\Users\\AtechM_03\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    chromedriver = link
    driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
    # self.tags_wait('body', 'input', 'div')

    # sleep(5)
    return driver


driver = _driver('I:\\MAE')
driver.get('https://drive.google.com/drive/folders/1tVI5Bxh2C1PjhXxGh020VTN7boTAZnGH')
driver.implicitly_wait(10)

login, senha = "39270@emeb.saobernardo.sp.gov.br", "Silas2804"

sleep(2)
ac = ActionChains(driver)
ac.send_keys(login)
ac.send_keys(Keys.ENTER)
ac.perform()

sleep(3)
ac = ActionChains(driver)
ac.send_keys(senha)
ac.send_keys(Keys.ENTER)
ac.perform()

for k, dictt in data.items():
    if k == 'Nome do aluno':
        for kk, aluno in dictt.items():
            if str(aluno).strip() != 'nan':
                print(aluno)
                driver.implicitly_wait(10)
                sleep(2.5)
                driver.get("https://docs.google.com/presentation/d/1W-tGjoTE0qf5mFiwg6iThzW8HHAHACtP5WyJHF9T7rM/")
                sleep(2)
                driver.find_element_by_id('docs-file-menu').click()
                # Fazer uma cópia c

                # driver.find_element_by_css_selector("[aria-label=Fazer uma cópia c]").click()
                sleep(1)
                ac = ActionChains(driver)
                for i in range(5):
                    ac.send_keys(Keys.DOWN)

                ac.send_keys(Keys.RIGHT)
                ac.send_keys(Keys.ENTER)
                ac.pause(1)
                ac.send_keys(f'{aluno} - 3ºD PORTIFÓLIO')
                ac.pause(1)
                ac.send_keys(Keys.ENTER)
                ac.pause(5)

                ac.pause(1)
                ac.perform()
                sleep(2.5)
                import pyautogui as pg
                pg.hotkey('ctrl', 'w')




