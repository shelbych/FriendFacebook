'''
Created on Aug 3, 2013

@author: Chuck Woodraska
'''


import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

def login(email, password):
    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys(email)
    inputElement = driver.find_element_by_id("pass")
    inputElement.send_keys(password)
    inputElement = driver.find_element_by_id("loginbutton")
    inputElement.click()

def logout():
    inputElement = driver.find_element_by_id("navAccountLink")
    inputElement.click()
    inputElement = driver.find_element_by_partial_link_text("Log Out")
    inputElement.click()

def friendSomebody():
    # put persons url here
    # go to there page and put there facebook copy the url and put it below
    driver.get("https://www.facebook.com/???????????")
    inputElement = driver.find_element_by_id("u_0_n")
    inputElement.click()
    #inputElement = driver.find_element_by_css_selector("div._586i").click()
    #inputElement2 = driver.find_element_by_name("q")
    #inputElement2.send_keys("julio madio\n")


email = ''
password = ''
# Load XML
tree = ET.parse('People.xml')
root = tree.getroot()

for person in root.iter('person'):
    driver = webdriver.Firefox()
    driver.get("http://www.facebook.com/")
    for info in person.iter():
        if(info.tag == 'email'):
            email = info.text
        elif(info.tag == 'password'):
            password = info.text
    login(email, password)
    
    #ACTION AREA
    friendSomebody()
    
     # Dont need logout when we close the browser and start a new session
    #logout()
    #driver.close()

            