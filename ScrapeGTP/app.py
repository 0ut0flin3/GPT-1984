
## BY 0ut0flin3 ################


import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from fake_useragent import UserAgent
op = webdriver.ChromeOptions()
op.add_argument(f"user-agent={UserAgent.random}")
op.add_argument("user-data-dir=./")
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])

##############################
##
## op.add_argument('headless')
##
## don't show the browser (it doesn't seem to work with undetected_chromedriver) ###
## 
###############################


driver = uc.Chrome(chrome_options=op)




def openai_login(MAIL,PASSWORD):
    driver.get('https://chat.openai.com/auth/login')
    time.sleep(5)
    inputElements = driver.find_elements(By.TAG_NAME, "button")
    inputElements[0].click()
    time.sleep(3)
    mail = driver.find_elements(By.TAG_NAME,"input")[1]
    mail.send_keys(MAIL)
    btn=driver.find_elements(By.TAG_NAME,"button")[0]
    btn.click()
    password= driver.find_elements(By.TAG_NAME,"input")[2]
    password.send_keys(PASSWORD)
    btn=driver.find_elements(By.TAG_NAME,"button")[1]
    btn.click()
    
def skip_popups():
    skip=driver.find_elements(By.TAG_NAME,"div")
    skip[45].click()
    skip=driver.find_elements(By.TAG_NAME,"div")
    try:
        skip[46].click()
    except:
        skip[45].click()
    skip=driver.find_elements(By.TAG_NAME,"div")
    skip[51].click()


def get_response(prompt):
    inputElements = driver.find_elements(By.TAG_NAME, "textarea")
    inputElements[0].send_keys(prompt)
    time.sleep(1)
    inputElements = driver.find_elements(By.TAG_NAME, "button")
    inputElements[3].click()
    inputElements = driver.find_elements(By.TAG_NAME, "div")
    time.sleep(5)
    response=inputElements[22].get_attribute('textContent')
    '''
    
    all_links=driver.find_elements(By.TAG_NAME, "a")
    for x in range(len(all_links)):
        if all_links[x].get_attribute('textContent')=='New chat':
           all_links[x].click()
    '''
    return response
    



openai_login("YOURMAIL","PASSWORD")
skip_popups()
response=get_response(' '.join(sys.argv[1:]))
print(response)
driver.close()



    



      
      

        

