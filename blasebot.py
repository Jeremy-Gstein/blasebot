import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
#Essential for driver + global vars
driver = webdriver.Firefox()
driver.get('https://www.blaseball.com/login')
betPage = 'https://www.blaseball.com/upcoming'

def Credentials():
    #Credentials for Blaseball.com
    loginEmail = open("/home/jeremyg/Scripts/Blasebot/BlasebotEmail.txt", "r")
    loginPass = open("/home/jeremyg/Scripts/Blasebot/Blasebotpass.txt", "r")
    #Email input
    usrname = driver.find_element_by_name("username") # Finds the email box
    usrname.send_keys(loginEmail.read())
    #Password input
    passwrd = driver.find_element_by_name("password") # Finds the password box
    passwrd.send_keys(loginPass.read())
def finishLogin():
    entercreds = driver.find_element_by_class_name("Auth-Submit") # Finds the continue button
    time.sleep(2) #Added delay to smooth login
    entercreds.click()
def firstBet():
    time.sleep(1)
    driver.get(betPage)
    driver.find_element_by_link_text("Place a Bet").click()
    time.sleep(1)
    driver.find_element_by_class_name("Bet-Form-Team-Name").click()
    time.sleep(1)
    driver.find_element_by_class_name("Bet-Form-Inputs-Amount-MaxBet").click()
    time.sleep(1)
    driver.find_element_by_class_name("Bet-Submit.btn.btn-success").click()


#GAME ONE HREF
gameOne = "https://www.blaseball.com/bet/12d9ad4a-9873-496f-81e1-e54e476a4727"


####PROGRAM-START####
#####-BLASEBOT-######
##WWW.BLASEBALL.COM##
Credentials()
finishLogin()
games = 0
while games < 10:
    firstBet()
