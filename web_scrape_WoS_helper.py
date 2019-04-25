# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:59:08 2019

@author: Kischy
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


standard_delay = 10
short_delay = 1


def open_web_of_science(driver):
    driver.get('https://apps.webofknowledge.com')


def search_on_web_of_science(driver,search_string):
    search_form = driver.find_element_by_id('value(input1)')
    search_form.send_keys(search_string)
    search_form.submit()
    

def click_on_element_by_id(driver,element_id):         
    WebDriverWait(driver, standard_delay).until(EC.presence_of_element_located((By.ID, "pageCount.bottom")))
    driver.implicitly_wait(short_delay)
    element = driver.find_element_by_id(element_id)    
    element.click()        


def get_times_cited_elements(driver):      
#    driver.implicitly_wait(short_delay)
    elements = driver.find_elements_by_class_name("snowplow-times-cited-link")
    return elements


def check_cited_elements(times_cited_elements, maxlength):
    if(len(times_cited_elements) > maxlength): 
        times_cited_elements.pop()
    

def get_times_cited_numbers(times_cited_elements):    
    times_cited = []
    
    for el in times_cited_elements:
        if el != '\n' and el != '':
            times_cited.append(int(el.text.replace(',','')))
        
    return times_cited





