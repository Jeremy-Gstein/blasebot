import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#Essential for driver + global vars
driver = webdriver.Firefox()
driver.get('https://www.blaseball.com/login')
betPage = 'https://www.blaseball.com/upcoming'
shopPage = 'https://blaseball.com/shop'

#Provides Login Credentials for Blaseball.com (CANNOT USE GOOGLE/APPLE/FACEBOOK)
def Credentials():
    #Credentials for Blaseball.com
    loginEmail = open("/home/jeremyg/Scripts/Blasebot/BlasebotEmail.txt", "r")
    loginPass = open("/home/jeremyg/Scripts/Blasebot/Blasebotpass.txt", "r")
    #Email input
    usrname = driver.find_element_by_name("username") #Finds the email box
    time.sleep(3)
    usrname.send_keys(loginEmail.read())
    #Password input
    passwrd = driver.find_element_by_name("password") #Finds the password box
    time.sleep(3)
    passwrd.send_keys(loginPass.read())
    entercreds = driver.find_element_by_class_name("Auth-Submit") #Submits the login credentials
    time.sleep(2)
    entercreds.click()

#Decides which team has the better win-percentage and selects the better team
def logic():
    time.sleep(1)
    away = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[2]/div[2]/div[3]").text
    home = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[1]/div[2]/div[3]').text
    convertAway = away.replace('%','')
    convertHome = home.replace('%','')
    awayPercentage = int(convertAway)
    homePercentage = int(convertHome)
    if awayPercentage > homePercentage:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[2]/div[2]/div[3]").click()
    else:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[1]/div[2]/div[3]').click()


#Places a max-bet on the favored team
def placeBet():
    time.sleep(3)
    driver.find_element_by_link_text("Place a Bet").click()
    time.sleep(1)
    logic()
    time.sleep(1)
    driver.find_element_by_class_name("Bet-Form-Inputs-Amount-MaxBet").click()
    time.sleep(1)
    driver.find_element_by_class_name("Bet-Submit.btn.btn-success").click()
    time.sleep(5)
    try:
        driver.find_element_by_class_name("Modal-Close").click()
    except NoSuchElementException:
        placeBet()

####PROGRAM-START####
#####-BLASE-BOT-#####
##WWW.BLASEBALL.COM##
Credentials()
time.sleep(1)
driver.get(betPage)
while True:
    placeBet()
