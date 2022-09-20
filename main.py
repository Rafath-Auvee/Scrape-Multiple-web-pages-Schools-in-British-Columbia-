from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException

delay = 15
element_list = []
href_list = []
email_list = []

try:
    for page in range(0, 23, 1):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        if page == 0:
            page_url = f"https://www.city-data.com/schools-dirs/schools-BC.html"
        else:
            page_url = f"https://www.city-data.com/schools-dirs/schools-BC{page}.html"
        driver.get(page_url)
        parentElement = driver.find_element(By.XPATH, '//*[@id="main_body"]/div[3]/div[2]/div/div/table/tbody')
        # print(parentElement)
        elementList = parentElement.find_elements(By.TAG_NAME, "a")
        for i, my_href in enumerate(elementList):
            myElem = my_href.get_attribute('href')
            email_url = myElem
            email_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            email_driver.get(email_url)
            emailElement = email_driver.find_element(By.XPATH, '//*[@id="main_body"]/div[3]/div[1]/div[1]/div[1]/div[1]')
            if len(email_driver.find_elements(By.XPATH, '//*[@id="main_body"]/div[3]/div[1]/div[1]/div[1]/div[1]/a')) > 0:
                result_email = emailElement.find_elements(By.XPATH, '//*[@id="main_body"]/div[3]/div[1]/div[1]/div[1]/div[1]/a')[ 0 ].text
            else:
                result_email = 'N/A'
            # print(i, result_email)
            element_list.append([elementList[i].text, result_email])
            email_driver.quit()
except TimeoutException:
    print("Loading took too much time!")
finally:
    driver.quit()
    print(element_list)

