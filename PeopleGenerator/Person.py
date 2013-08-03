'''
Created on Jul 16, 2013

@author: Chuck Woodraska
'''
import random
import time
import datetime


class Person:
    """A simple example class"""
    firstName = ''
    lastName = ''
    sex = 0
    birthday = datetime.date(1995,11,1)
    password = ''
    email = ''
    
    def printPerson(self):
        print(self.firstName)
        print(self.lastName)
        print(self.sex)
        print(self.birthday)
        print(self.password)
        print(self.email)
    
    def generateFirstName(self, listName, size):
        file = open(listName+'.txt')
        lines = file.readlines()
        tempName = lines[random.randint(0,size-1)]
        tempNameSplit = tempName.split('\n')
        self.firstName = tempNameSplit[0]
    
    def generateLastName(self):
        file = open('last.txt')
        lines = file.readlines()
        tempName = lines[random.randint(0,99)]
        tempNameSplit = tempName.split('\n')
        self.lastName = tempNameSplit[0]
    
    def generateBirthday(self):
        def date_to_timestamp(d) :
            return int(time.mktime(d.timetuple()))

        def randomDate(start, end):
            """Get a random date between two dates"""
            
            stime = date_to_timestamp(start)
            etime = date_to_timestamp(end)
            
            ptime = random.randrange(stime,etime)
            
            return datetime.date.fromtimestamp(ptime)
        start = datetime.date(1973,1,1)
        end = datetime.date(1995,12,31)
        self.birthday = randomDate(start, end)

    
    def generateSex(self):
        self.sex = random.randint(0,1)
        if self.sex == 0:
            self.generateFirstName("female",521)
        else:
            self.generateFirstName("male",516)
    
    def generatePassword(self):
        for x in range(32):
            self.password = self.password + random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321')
    
    def generateEmail(self):
        for x in range(24):
            self.email = self.email + random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321')
        self.email = self.email + '@mt2014.com'
        
    def generatePerson(self):
        self.generateSex()
        self.generateLastName()
        self.generateBirthday()
        self.generatePassword()
        self.generateEmail()
        