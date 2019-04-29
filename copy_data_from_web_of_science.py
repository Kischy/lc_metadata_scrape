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
export.send_keys("500")

driver.implicitly_wait(short_delay)

#export = driver.find_element_by_xpath("//span[@id='select2-bib_fields-container']")
#export.click()

driver.implicitly_wait(short_delay)

record = driver.find_element_by_xpath("//span[@id='select2-bib_fields-container']")
record.click()

secondLevelMenu = driver.find_elements_by_xpath("//*[text()[contains(., 'Full Record and Cited References')]]");
secondLevelMenu[2].click()


#driver.implicitly_wait(short_delay)

record = driver.find_element_by_xpath("//span[@id='select2-saveOptions-container']")
record.click()

secondLevelMenu = driver.find_elements_by_xpath("//*[text()[contains(., 'Plain Text')]]");
secondLevelMenu[4].click()


export = driver.find_element_by_xpath("//button[@id='exportButton']")
export.click()



#action.move_to_element(secondLevelMenu).perform()

#secondLevelMenu.click()



#export.find_element_by_xpath("//span[@aria-activedescendant='select2-bib_fields-result-eptz-HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  ']").click()




#record = driver.find_element_by_name("fields_selection")

#record.location_once_scrolled_into_view
#record.click()
#record.click()

#record = driver.find_element_by_name("fields_selection")

#driver.execute_script("arguments[0].click();",record)

#record_content = Select(driver.find_element_by_xpath("//select[@id='bib_fields']"))

#record_content.select_by_index(3)

#export.find_element_by_xpath("//span[.='Full Record and Cited References']").click()

#export.find_element_by_xpath("//*[text()[contains(., 'Full Record and Cited References')]]").click()

#driver.implicitly_wait(short_delay)


#record_content = Select(driver.find_element_by_name("fields_selection"))
#
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By., "fields_selection")))
#
#record_content.select_by_index(3)



#export = driver.find_element_by_xpath("//select[@id='bib_fields']")
#select_box = Select(export)
#select_box.select_by_index(3)
#
#driver.implicitly_wait(short_delay)





#elements[0].click()

#driver.quit()