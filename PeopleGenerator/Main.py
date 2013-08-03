'''
Created on Jul 16, 2013

@author: Chuck Woodraska
'''
from Person import Person
import xml.etree.ElementTree as ET

root = ET.Element("root")

for x in range(10):
    tempPerson = Person()
    tempPerson.generatePerson()
    tempPerson.printPerson()
    person = ET.SubElement(root, "person")

    firstName = ET.SubElement(person, "firstName")
    firstName.text = tempPerson.firstName
    lastName = ET.SubElement(person, "lastName")
    lastName.text = tempPerson.lastName
    sex = ET.SubElement(person, "sex")
    sex.text = str(tempPerson.sex)
    birthday = ET.SubElement(person, "birthday")
    birthday.text = str(tempPerson.birthday)
    email = ET.SubElement(person, "email")
    email.text = tempPerson.email
    password = ET.SubElement(person, "password")
    password.text = tempPerson.password
    
tree = ET.ElementTree(root)
tree.write("People.xml")
