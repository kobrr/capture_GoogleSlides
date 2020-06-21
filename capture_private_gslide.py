# -*- coding: utf-8 -*-
import os, sys,re
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# seems to be effective to maxretryerrorDesiredCapabilities
# avoid SessionNotCreatedException
from webdriver_manager.chrome import ChromeDriverManager

def capture_gslide(chromedriver_path, gslide_url, save_folder):
    """ take screenshots of Google Slide
    """
    # avoid SessionNotCreatedException
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(gslide_url)
    time.sleep(3)

    actions = ActionChains(driver)
    actions.send_keys(Keys.END)
    actions.perform()
    time.sleep(3)

    # get the number of slides
    contents = driver.find_elements_by_xpath('.//*[@id="filmstrip"]')
    lst = [i.text for i in contents][0].split('\n')
    lst = [int(i) for i in lst if re.match(r'[0-9]+', i)]
    max_pages = max(lst)
    print('the number of slides: ', max_pages)
    time.sleep(3)

    # click on Present button and start Present from 1st slide
    present_pulldown =  driver.find_element_by_xpath('.//*[@id="punch-start-presentation-right"]')
    present_pulldown.click()
    time.sleep(3)
    start_present =  driver.find_element_by_xpath('.//*[@id=":31"]')
    start_present.click()
    time.sleep(10)

    # move to next page until the end
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN)
    counter = 1
    while counter < max_pages:
        counter += 1
        fname = '{}.png'.format(str(counter).zfill(2))
        save_dir = os.path.join(save_folder, fname)
        driver.save_screenshot(save_dir)
        print('Page ' + str(counter) + ' was captured.')
        time.sleep(2)
        actions.perform()

    print('DONE')

if __name__ == "__main__":
    args = sys.argv
    capture_gslide(args[1], args[2], args[3])
