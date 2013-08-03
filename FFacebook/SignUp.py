'''
Created on Jul 26, 2013

@author: Chuck Woodraska
'''


import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.Firefox()

# Load XML
tree = ET.parse('People.xml')
root = tree.getroot()

year = 0
month = 0
day = 0

for person in root.iter('person'):
    driver.get("http://www.facebook.com/")
    for info in person.iter():
        if(info.tag == 'firstName'):            
            inputElement = driver.find_element_by_id("u_0_0")
            inputElement.send_keys(info.text)
        elif(info.tag == 'lastName'):
            inputElement = driver.find_element_by_id("u_0_1")
            inputElement.send_keys(info.text)
        elif(info.tag == 'email'):
            inputElement = driver.find_element_by_id("u_0_2")
            inputElement.send_keys(info.text)
            inputElement = driver.find_element_by_id("u_0_3")
            inputElement.send_keys(info.text)
        elif(info.tag == 'password'):
            inputElement = driver.find_element_by_id("u_0_4")
            inputElement.send_keys(info.text)
        elif(info.tag == 'birthday'):
            tempBirthday = info.text
            birthdayList = tempBirthday.split('-')
            month = int(birthdayList[1])
            day = int(birthdayList[2])
            year = 2014-int(birthdayList[0])
            print(month)
            print(day)
            print(year)
        elif(info.tag == 'sex'):
            if(info.text == '0'):
                inputElement = driver.find_element_by_id("u_0_5")
                inputElement.click()
            else:
                inputElement = driver.find_element_by_id("u_0_6")
                inputElement.click()
            #driver.get("http://www.mytrashmail.com/")
            #inputElement = driver.find_element_by_id("ContentPlaceHolder2_txtAccount")
            #inputElement.send_keys("Cheese!")
            #inputElement = driver.find_element_by_id("ContentPlaceHolder2_cmdGetMail")
            #inputElement.click()
            #print (info.text)
    inputElement = driver.find_element_by_id("month")
    allOptions = inputElement.find_elements_by_tag_name("option")
    option = allOptions[month]
    option.click()
    inputElement = driver.find_element_by_id("day")
    allOptions = inputElement.find_elements_by_tag_name("option")
    option = allOptions[day]
    option.click()
    inputElement = driver.find_element_by_id("year")
    allOptions = inputElement.find_elements_by_tag_name("option")
    option = allOptions[year]
    option.click()
    inputElement = driver.find_element_by_id("u_0_7")
    inputElement.click()
            