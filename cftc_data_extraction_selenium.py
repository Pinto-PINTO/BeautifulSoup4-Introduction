# Selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# Preventing Window from opening
options = Options()
options.add_argument('--headless')


# Driver
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

url = "https://a1trading.com/market-analysis/cot/"
driver.get(url)

# wait = WebDriverWait(driver, 10)    
# wait.until(EC.presence_of_element_located((By.TAG_NAME, "ng2-canvas-container")))

page_source = driver.page_source
doc = BeautifulSoup(page_source, "html.parser")

table_data = doc.div
print(table_data)