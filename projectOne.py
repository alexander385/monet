from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
#Type desired search phrase
#f = open("beispieltext.txt", "r")
#alex = f.read()
alex = input("Bitte Suchanfrage eingeben ")
driver = webdriver.Chrome('/Users/alexfrankow/Desktop/chromedriver')
driver.implicitly_wait(10)
#Accept the google cookies first
driver.get("https://google.de")
driver.find_element_by_id("L2AGLb").click()
time.sleep(5)
#Search for the given phrase
search_box = driver.find_element_by_name('q')
search_box.send_keys(alex)
search_box.submit()
time.sleep(5)
#Extract title and link
results = driver.find_elements_by_css_selector('div.g')
link = results[0].find_element_by_tag_name("a")
href = link.get_attribute("href")
driver.get(href)
# Getting current URL source code
get_title = driver.title
# Printing the title of this URL
print(get_title)
print(href)
#Close Browser
driver.quit()
