import json
from selenium import webdriver
import time
import random

def lambda_handler(event, context):
    body_temp = str(36 + random.randint(1,7)/10)
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScGgZ8dsBkcSVutvW3JgDLqy3pIEKk12ucjiA8mNQrKopILog/viewform?usp=pp_url&entry.1534939278=%E5%85%AB%E8%B0%B7%E8%88%AA%E5%A4%AA&entry.511939456='+body_temp
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/headless-chrome/headless-chromium'
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--single-process")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/opt/headless-chrome/chromedriver',options = options)
    driver.implicitly_wait(1)
    driver.get(url)
    
    def click(xpath):
        driver.find_element_by_xpath(xpath).click()

    def insert_pw(xpath, str):
        driver.find_element_by_xpath(xpath).send_keys(str)
    
    moving_login_button = '/html/body/div[2]/div/div[2]/div[3]/div[2]'
    time.sleep(2)
    if(driver.find_elements_by_xpath(moving_login_button) != []):
        click(moving_login_button)
        login_id = MY_GMAIL
        login_id_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
        login_id_button = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div'
        insert_pw(login_id_xpath, login_id)
        click(login_id_button)
        time.sleep(1)
        login_pw = MY_PASSWORD
        login_pw_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
        login_pw_button = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div'
        insert_pw(login_pw_xpath, login_pw)
        time.sleep(1)
        click(login_pw_button)
    time.sleep(1)
    submit_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div'
    click(submit_button)
    driver.close
    driver.quit
    return {
        'statusCode': 200,
        'body': json.dumps('Form submission success!!')
    }
