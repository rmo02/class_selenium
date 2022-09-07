from selenium import webdriver
import time;

chrome = webdriver.Chrome("C:/Users/rmo02/teste e qualidade/Teste2/chromedriver/chromedriver.exe")

chrome.get('https://undbclassroom.undb.edu.br/')
time.sleep(3)

# localizando user e passando user
chrome.findElement(By.id(“id”)).send_keys('002-022771')

# localizando senha e passando password
chrome.findElement(By.XPATH,(
    "//*[@id="password"]")).send_keys("RamonMaia1")


# submit
chrome.find_element(By.ID,
    "loginbtn").click()
