import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#Essential for driver + global vars
driver = webdriver.Firefox()
betPage = 'https://www.blaseball.com/upcoming'
shopPage = 'https://www.blaseball.com/shop'
logOut = 'https://www.blaseball.com/auth/logout'

#Provides Login Credentials for Blaseball.com (CANNOT USE GOOGLE/APPLE/FACEBOOK)
#For best results it is HIGHLY recommended you manually zoom out your automated browser to 30%.
#Currently working to hardcode this but zooming in/out is a known issue mentioned in the GeckoDriver docs.
def Credentials():
    #Credentials for Blaseball.com.
    driver.get('https://www.blaseball.com/login')
    driver.maximize_window()
    time.sleep(2)
    #Create two different textfiles with your blasebot credentials and provide their unique path.
    loginEmail = open(r"C:\Path\To\Email\Text-File\BlasebotEmail.txt", mode='r')
    loginPass = open(r"C:\Path\To\Password\Text-File\Blasebotpass.txt", mode='r')
    #Email input:
    time.sleep(10)
    #Finds the email box.
    usrname = driver.find_element_by_name("username")
    time.sleep(3)
    usrname.send_keys(loginEmail.read())
    #Password input:
    #Finds the password box.
    passwrd = driver.find_element_by_name("password")
    time.sleep(3)
    passwrd.send_keys(loginPass.read())
    time.sleep(3)
    #Submits the login credentials.
    entercreds = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/form/div[3]/input")
    time.sleep(5)
    entercreds.click()

#Decides which team has the better win-percentage and selects the better team.
def logic():
    time.sleep(3)
    away = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/form/div[1]/div[1]/div[2]/div[3]").text
    home = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/form/div[1]/div[2]/div[2]/div[3]").text
    time.sleep(5)
    convertAway = away.replace('%','')
    convertHome = home.replace('%','')
    awayPercentage = int(convertAway)
    homePercentage = int(convertHome)
    if awayPercentage > homePercentage:
        awayTeam = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/form/div[1]/div[1]/div[2]/div[3]").click()
    else:
         homeTeam = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/form/div[1]/div[2]/div[2]/div[3]").click()

#Places a max-bet on the favored team.
def placeBet():
    time.sleep(3)
    driver.find_element_by_partial_link_text("Place a Bet").click()
    time.sleep(1)
    logic()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/form/div[2]/div/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/form/div[4]/button').click()
    time.sleep(5)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/form/div[4]/button')
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/button/svg/path').click()
    except NoSuchElementException:
        placeBet()

#Currently not in use but can be added with main functions to beg when out of currency.
def beg():
    driver.get(shopPage)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div[9]/div[3]/div[2]/button').click() #BEG BUTTON
    time.sleep(3)

#Currently not in use but can be added with main functions to beg when out of currency.
def checkCurrency():
    currency = driver.find_element_by_xpath('/html/body/div[1]/div/nav/div[3]/div[1]/a').text
    currentCurrency = int(currency)
    if currentCurrency == 0:
        beg()

#Rotates every 120 seconds to a different site while waiting for bets.
def waitingForBets():
    driver.get('https://www.blaseball.com')
    time.sleep(120)
    driver.get('https://www.blaseball.com/standings')
    time.sleep(120)
    driver.get('https://www.blaseball.com/bulletin')
    time.sleep(120)
    driver.get(logOut)
    time.sleep(10)
    driver.get('https://twitter.com/blaseball')
    time.sleep(120)
    driver.get(logOut)
    time.sleep(5)

#Recalls the main functions when an exception occurs. 
def recallStack():
    Credentials()
    time.sleep(1)
    driver.get(betPage)
    time.sleep(3)
    try:
        while True:
            placeBet()
    except NoSuchElementException:
        waitingForBets()
        time.sleep(120)
        recallStack()

print('''
 ___    _                        ___           _
(  _`\ (_ )                     (  _`\        ( )_
| (_) ) | |    _ _   ___    __  | (_) )   _   | ,_)
|  _ <' | |  /'_` )/',__) /'__`\|  _ <' /'_`\ | |
| (_) ) | | ( (_| |\__, \(  ___/| (_) )( (_) )| |_
(____/'(___)`\__,_)(____/`\____)(____/'`\___/'`\__)
___________________________________________________
               By:Shodo, HWS Devteam
                  Windows Edition
''')

try:
    Credentials()
    time.sleep(5)
    driver.get(betPage)
    time.sleep(5)
    try:
        while True:
            placeBet()
    except NoSuchElementException:
        #checkCurrency()
        waitingForBets()
        time.sleep(120) #15 mins = 900 sec
        recallStack()
except NoSuchElementException:
    driver.get(logOut)
    time.sleep(5)
    recallStack()
