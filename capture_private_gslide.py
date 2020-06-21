# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# seems to be effective to maxretryerror
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# to avoid SessionNotCreatedException
from webdriver_manager.chrome import ChromeDriverManager

def capture_gslide(chromedriver_path, gslide_url):
    """
    """
    # unavailable for download the slide
    driver = webdriver.Chrome(ChromeDriverManager().install()) # to avoid SessionNotCreatedException
    driver.implicitly_wait(10)
    driver.get(gslide_url)
    time.sleep(3)

    actions = ActionChains(driver)
    actions.send_keys(Keys.END)
    actions.perform()
    time.sleep(3)


    contents = driver.find_elements_by_xpath('.//*[@id="filmstrip"]')
    lst = [i.text for i in contents][0].split('\n')
    lst = [int(i) for i in lst if re.match(r'[0-9]+', i)]
    max_pages = max(lst)
    print(max_pages)
    time.sleep(3)

    # click on Present button and start Present 1st slide
    present_pulldown =  driver.find_element_by_xpath('.//*[@id="punch-start-presentation-right"]')
    present_pulldown.click()
    time.sleep(3)
    start_present =  driver.find_element_by_xpath('.//*[@id=":31"]')
    start_present.click()
    time.sleep(3)

    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN)
    counter = 1
    while counter < max_pages:
        actions.perform()
        counter += 1
        driver.save_screenshot('{}.png'.format(str(counter).zfill(2)))
        time.sleep(2)
        print('Page ' + counter + ' was captured')

    print('DONE')


