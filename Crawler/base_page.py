import traceback, re,  pybase64, json, time, os

from enum import Enum as _Enum
from hashlib import sha256
from typing import List
from random import randint

from selenium import webdriver as im_webdriver
from selenium.webdriver.support import expected_conditions as im_expected_conditions
from selenium.common import exceptions as im_selexc
from selenium.webdriver.common.touch_actions import TouchActions


class BasePage:

    def open_explore(self, target_url: str, target_path: str, user_agent: str, win_width: int = 0, win_height: int = 0, win_ratio: int = 0):

        self.target_path = target_path
        self.target_url = target_url

        desired_caps = im_webdriver.DesiredCapabilities.CHROME.copy()
        my_chrome_option = im_webdriver.ChromeOptions()

        my_chrome_option.add_argument('--incognito')
        my_chrome_option.add_argument('--disable-infobars')
        my_chrome_option.add_argument('--disable-plugins')
        my_chrome_option.add_argument('--hide-scrollbars')
        my_chrome_option.add_argument('--ignore-certificate-errors')
        my_chrome_option.add_argument('--disable-application-cache')

        fullPath = os.path.abspath(self.target_path)
        my_chrome_option.add_argument('--disk-cache-dir=' + fullPath + '\\disk-cache-dir')
        my_chrome_option.add_argument('--user-data-dir=' + fullPath + '\\user-data-dir')
        my_chrome_option.binary_location = 'C:\\chrome\\chrome.exe'
        
        my_chrome_option.add_experimental_option('w3c', False)
        my_chrome_option.add_argument('--log-level=3')
        my_chrome_option.add_argument('--headless')
        my_chrome_option.add_argument('--disable-gpu')
        my_chrome_option.add_argument('--disable-software-rasterizer')
        my_chrome_option.add_argument('--disable-smooth-scrolling')
        my_chrome_option.add_argument('--use-fake-mjpeg-decode-accelerator')
        my_chrome_option.add_argument('--use-file-for-fake-audio-capture')
        my_chrome_option.add_argument('--use-file-for-fake-video-capture')
        my_chrome_option.add_argument('--disable-blink-features')
        my_chrome_option.add_argument('--disable-blink-features=AutomationControlled')
        my_chrome_option.add_argument('--disable-notifications')
        my_chrome_option.add_experimental_option('prefs', {"profile.managed_default_content_settings.images":2})
        my_chrome_option.add_experimental_option('prefs', {"profile.default_content_setting_values" : {"notifications" : 2}})
        my_chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])
        my_chrome_option.add_experimental_option('useAutomationExtension', False)
        my_chrome_option.add_experimental_option('prefs', {'profile.password_manager_enabled': False, 'credentials_enable_service': False})

        mobileEmulation = {"deviceMetrics": {"width": win_width, "height": win_height, "pixelRatio": win_ratio}, "userAgent": user_agent}
        my_chrome_option.add_experimental_option('mobileEmulation', mobileEmulation)

        self.web_driver = im_webdriver.Chrome(\
            executable_path = '.\\Tools\\Chrome_Driver\\chromedriver.exe', \
            desired_capabilities = desired_caps, \
            options = my_chrome_option)

        self.web_driver.get(target_url)
        self.wait_dom(self.web_driver)


    def close_explore(self):
        self.web_driver.quit()


    def wait_dom(self, web_driver) -> None:
        while(True):
            if (web_driver.execute_script('return document.readyState') != 'loading') and\
               (web_driver.execute_script('return document.body != null;')):
               break

            time.sleep(1)


    def get_all_data(self):
        table = self.web_driver.find_element_by_xpath('//*[@id="thetable"]/tbody')
        rows = table.find_elements_by_tag_name('tr')

        result = list()

        for row_idx in range(0, len(rows)):
            ths = rows[row_idx].find_elements_by_tag_name('th')
            tds = rows[row_idx].find_elements_by_tag_name('td')

            if len(ths) < 2 or len(tds) < 3:
                continue
            
            try:
                country = ths[1].find_element_by_tag_name('a').get_attribute('textContent')
                cases = re.sub('[\xc2\xa0]', ' ', re.sub('[\r\n\t]', '', tds[0].get_attribute('textContent')))
                deaths = re.sub('[\xc2\xa0]', ' ', re.sub('[\r\n\t]', '', tds[1].get_attribute('textContent')))
                recover = re.sub('[\xc2\xa0]', ' ', re.sub('[\r\n\t]', '', tds[2].get_attribute('textContent')))
                
                result.append({"Country": country, "Cases": cases, "Deaths": deaths, "Recover": recover})

            except im_selexc.StaleElementReferenceException:
                continue

        return result