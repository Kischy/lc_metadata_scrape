# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:53:01 2019

@author: Kischy
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By



import web_scrape_WoS_helper as hp


firefox_binary_exe_path = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
driver_exe_path = r"C:\\Cloud 2\\Programmierung\\Python\\geckodriver\\geckodriver.exe"
standard_delay = 10
short_delay = 1



binary = FirefoxBinary(firefox_binary_exe_path)

opts = Options()
#opts.headless = True
#assert opts.headless  # Operating in headless mode

driver = Firefox(firefox_binary=binary, executable_path=driver_exe_path,options=opts)
#driver.implicitly_wait(30)

hp.open_web_of_science(driver)
hp.search_on_web_of_science(driver,"\"liquid crystal\"")


times_cited_id = r"LC.D;PY.D;AU.A.en;SO.A.en;VL.D;PG.A"
hp.click_on_element_by_id(driver,times_cited_id)


elements = hp.get_times_cited_elements(driver)
hp.check_cited_elements(elements,10)
#times_cited = hp.get_times_cited_numbers(elements)

export = driver.find_element_by_xpath("//button[@id='exportTypeName']")
export.click()

driver.implicitly_wait(short_delay)

export = driver.find_element_by_xpath("//a[@name='Export to Other File Formats']")
export.click()

driver.implicitly_wait(short_delay)


export = driver.find_element_by_xpath("//input[@id='numberOfRecordsRange']")
export.click()

driver.implicitly_wait(short_delay)


export = driver.find_element_by_xpath("//input[@id='markFrom']")
export.clear()
export.send_keys("1")

driver.implicitly_wait(short_delay)


export = driver.find_element_by_xpath("//input[@id='markTo']")
export.clear()
export.send_keys("1")

driver.implicitly_wait(short_delay)

export = driver.find_element_by_xpath("//span[@id='select2-bib_fields-container']")
export.click()
driver.implicitly_wait(short_delay)

export = driver.find_element_by_xpath("//select[@id='bib_fields']")
select_box = Select(export)
select_box.select_by_index(3)

driver.implicitly_wait(short_delay)





#elements[0].click()

#driver.quit()