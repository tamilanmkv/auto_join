#!/bin/python3 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import time
import datetime



opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})
##informations 

username = input("Enter Gmail ID: ")
password = input("password: ")
meet = input("Meet ID: ")
mtime = input("Meet Time: ")


def account(driver, username, password):
    driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27")
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    time.sleep(2)
    google(meet)

def google(meet):
      # #opening Meet:

    driver.get(meet)
    time.sleep(4)
        # Turning off video
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    time.sleep(5)
        # turnime.sleep(180)
        # Join class
        #dring off audio
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    time.sleep(8)
        # Join class
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]').click()


#timing
def amaithi(mtime):
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time == mtime:
            break
    ##browser       
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    account(driver, username, password)
    return 0

amaithi(mtime)
