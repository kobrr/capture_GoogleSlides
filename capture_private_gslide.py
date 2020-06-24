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


def capture_gslide(chromedriver_path, gslide_url, max_page_no, save_folder=''):
    """ take screenshots of Google Slide
        max_page_no: int
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

    # TODO:
    # get the number of slides ← different btwn each slide
    # contents = driver.find_elements_by_xpath('.//*[@id="filmstrip"]')
    # lst = [i.text for i in contents][0].split('\n')
    # lst = [int(i) for i in lst if re.match(r'[0-9]+', i)]
    # max_page_no = max(lst)
    # print('the number of slides: ', max_page_no)
    # time.sleep(3)

    # click on Present button and start Present from 1st slide
    # present_pulldown =  driver.find_element_by_xpath('.//*[@id="punch-start-presentation-right"]')
    # present_pulldown.click()
    # time.sleep(3)

    # start the presentation
    keys = Keys()
    actions = ActionChains(driver)
    actions.send_keys(keys.COMMAND + keys.SHIFT + keys.ENTER)
    actions.key_down(keys.SHIFT).key_down(keys.COMMAND).send_keys(keys.ENTER)
    actions.perform()
    time.sleep(8)

    # move to next page until the end
    # pressing PAGE_DOWN or ENTER seems not to work
    actions = ActionChains(driver)
    actions.click()
    counter = 1
    while counter <= int(max_page_no):
        fname = '{}.png'.format(str(counter).zfill(2))
        save_dir = os.path.join(save_folder, fname)
        driver.save_screenshot(save_dir)
        print('Page ' + str(counter) + ' was captured.')
        actions.perform()
        counter += 1
        time.sleep(2)


    print('DONE')

if __name__ == "__main__":
    args = sys.argv
    capture_gslide(args[1], args[2], args[3])
