# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:59:08 2019

@author: Kischy
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


standard_delay = 10
medium_delay = 3
short_delay = 1


def open_web_of_science(driver):
    driver.get('https://apps.webofknowledge.com')


def search_on_web_of_science(driver,search_string):
    search_form = driver.find_element_by_id('value(input1)')
    search_form.send_keys(search_string)
    search_form.submit()
    

def click_on_element_by_id(driver,element_id):         
    WebDriverWait(driver, standard_delay).until(EC.presence_of_element_located((By.ID, "pageCount.bottom")))
    driver.implicitly_wait(medium_delay)
    element = driver.find_element_by_id(element_id)    
    element.click()        


def get_times_cited_elements(driver):      
#    driver.implicitly_wait(short_delay)
    elements = driver.find_elements_by_class_name("snowplow-times-cited-link")
    return elements

def get_number_of_results(driver):      
#    driver.implicitly_wait(short_delay)
    results = driver.find_element_by_xpath("//span[@id='hitCount.top']")    
    results = results.get_attribute("innerHTML") 
    result = int(results.replace(',',''))
    return result


def check_cited_elements(times_cited_elements, maxlength):
    if(len(times_cited_elements) > maxlength): 
        times_cited_elements.pop()
    

def get_times_cited_numbers(times_cited_elements):    
    times_cited = []
    
    for el in times_cited_elements:
        if el != '\n' and el != '':
            times_cited.append(int(el.text.replace(',','')))
        
    return times_cited



def download_records_first(driver, from_rec, to_rec):    
    driver.implicitly_wait(short_delay)

    export = driver.find_element_by_xpath("//button[@id='exportTypeName']")
    export.click()
    
    driver.implicitly_wait(short_delay)
    
    export = driver.find_element_by_xpath("//a[@name='Export to Other File Formats']")
    export.click()
    
    download_rec_open(driver, from_rec, to_rec)



def download_records(driver, from_rec, to_rec):    
    driver.implicitly_wait(short_delay)

    export = driver.find_element_by_xpath("//button[@title='Export the selected records to a tab-delimited file, other reference software, and more']")
    export.click()
    
    download_rec_open(driver, from_rec, to_rec)




def download_rec_open(driver, from_rec, to_rec):
    driver.implicitly_wait(short_delay)    
    
    number_records = driver.find_element_by_xpath("//input[@id='numberOfRecordsRange']")
    number_records.click()
    
    driver.implicitly_wait(short_delay)
        
    from_record = driver.find_element_by_xpath("//input[@id='markFrom']")
    from_record.clear()
    from_record.send_keys(from_rec)
    
    driver.implicitly_wait(short_delay)
    
    
    to_record = driver.find_element_by_xpath("//input[@id='markTo']")
    to_record.clear()
    to_record.send_keys(to_rec)
    
    driver.implicitly_wait(short_delay)
    
    
    record_content = driver.find_element_by_xpath("//span[@id='select2-bib_fields-container']")
    record_content.click()
    
    record_content_secondLevelMenu = driver.find_elements_by_xpath("//*[text()[contains(., 'Full Record and Cited References')]]");
    record_content_secondLevelMenu[2].click()
    
        
    save_option = driver.find_element_by_xpath("//span[@id='select2-saveOptions-container']")
    save_option.click()
    
    save_option_secondLevelMenu = driver.find_elements_by_xpath("//*[text()[contains(., 'Plain Text')]]");
    save_option_secondLevelMenu[4].click()
    
    
    export = driver.find_element_by_xpath("//button[@id='exportButton']")
    export.click()
    
    driver.implicitly_wait(medium_delay)
    driver.implicitly_wait(medium_delay)

    close_but = driver.find_element_by_xpath("//a[@class='flat-button quickoutput-cancel-action']")
    close_but.click()
    





