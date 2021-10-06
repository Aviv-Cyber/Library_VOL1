import pandas as pd
import os
import pyautogui
import csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart

df = pd.read_csv('Countries_Price_Attraction (1).csv')
COUNTRY = df.iloc[:, 0].values
COL = df.iloc[:, 1].values
ACTIVITY1 = df.iloc[:, 2].values
ACTIVITY2 = df.iloc[:, 3].values
ACTIVITY3 = df.iloc[:, 4].values
ACTIVITY4 = df.iloc[:, 5].values
ACTIVITY5 = df.iloc[:, 6].values
ACTIVITY6 = df.iloc[:, 7].values
ACTIVITY7 = df.iloc[:, 8].values
ACTIVITY8 = df.iloc[:, 9].values
ACTIVITIES = [ACTIVITY1, ACTIVITY2, ACTIVITY3 , ACTIVITY4, ACTIVITY5, ACTIVITY6, ACTIVITY7, ACTIVITY8]


driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get('https://www.skyscanner.co.il/transport/flights/tlv/lca/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27543994&inboundaltsenabled=false&infants=0&originentityid=27546296&outboundaltsenabled=false&oym=2107&preferdirects=false&preferflexible=false&ref=home&rtn=0&selectedoday=01')

ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()












"""
google_query = r'http://www.google.com/search?q='+ "hi man"
#Setting ticket prices paths
P1 = r'//*[@id="app-root"]/div/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/button/div[2]'
P2 = r'//*[@id="app-root"]/div/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[6]/button/div[2]'

def price_chooser(price):

    try:
        price_option = browser.find_element_by_xpath(price)
        price_option.click()
    except Exception as e:
        pass


for i in COUNTRY:
     1.get all top 10 places of each country.
     2.get all flights to i from israel for e.g
     3.get routes from the i main airport to every item from the top 10s lists.
     4.keep thinking of functions



get urlib and other libraries to make manipulations on the csv from websites like:
skyscanner, tripguard, tripadvisor, maps, square.
intgrate the data from the csv to actual information this websites has to offer.
"""