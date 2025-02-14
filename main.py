import time
import statics
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
service = Service("/usr/bin/chromedriver")  # مسیر chromedriver رو مشخص کن

driver = webdriver.Chrome(service=service, options=options)
driver.get(statics.SITE_ADDRESS)

btn = driver.find_element(By.NAME, 'txtbSearch')
btn.send_keys(statics.CODE)
btn.send_keys(Keys.ENTER)

result_panel = driver.find_elements(By.ID, 'pnlResult')
print(len(result_panel))

print(result_panel[0].text, end='\n\n')

time.sleep(80)

