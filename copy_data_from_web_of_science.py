# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:53:01 2019

@author: Kischy
"""

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.action_chains import ActionChains

import web_scrape_WoS_helper as hp



profile = webdriver.FirefoxProfile()
#profile.set_preference("browser.download.folderList", 2)
#profile.set_preference("browser.download.manager.showWhenStarting", False)
#profile.set_preference("browser.download.dir", 'PATH TO DESKTOP')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")

#https://stackoverflow.com/questions/25251583/downloading-file-to-specified-location-with-selenium-and-python

firefox_binary_exe_path = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
driver_exe_path = r"C:\\Cloud 2\\Programmierung\\Python\\geckodriver\\geckodriver.exe"
standard_delay = 10
short_delay = 1


binary = FirefoxBinary(firefox_binary_exe_path)

opts = Options()
#opts.headless = True
#assert opts.headless  # Operating in headless mode

driver = Firefox(firefox_binary=binary, executable_path=driver_exe_path,options=opts,firefox_profile=profile)
action = ActionChains(driver);

#driver.implicitly_wait(30)

hp.open_web_of_science(driver)
hp.search_on_web_of_science(driver,"\"liquid crystal\"")


times_cited_id = r"LC.D;PY.D;AU.A.en;SO.A.en;VL.D;PG.A"
hp.click_on_element_by_id(driver,times_cited_id)


elements = hp.get_times_cited_elements(driver)
hp.check_cited_elements(elements,10)
#times_cited = hp.get_times_cited_numbers(elements)



No_of_results = hp.get_number_of_results(driver)





#hp.download_records_first(driver,"2","399")

#hp.download_records(driver,"2","23")



#driver.quit()