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

rect_tag = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//rect[@x="67" and @y="25" and @width="819" and @height="37" and @stroke="none" and @stroke-width="0" and @fill="#3f48cc"]')))

# wait = WebDriverWait(driver, 10)    
# wait.until(EC.presence_of_element_located((By.TAG_NAME, "ng2-canvas-container")))

# page_source = driver.page_source
# doc = BeautifulSoup(page_source, "html.parser")

# table_data = doc.div
# rect_tag = doc.find_all(["g"])
# print(rect_tag)


# Check if the rect tag is present
if rect_tag:
    print("Rect tag found!")
else:
    print("Rect tag not found.")


# elements = driver.find_elements_by_xpath("//*[@clip-path]")

# for element in elements:
#     if element.get_attribute("clip-path") == "url(https://lookerstudio.google.com/embed/u/0/reporting/9dcc8738-fdf8-49db-b8d9-7beea9303f78/page/69G1C#_ABSTRACT_RENDERER_ID_3)":
#         print("Attribute found!")
#         break
# else:
#     print("Attribute not found.")

# from bs4 import BeautifulSoup
# import requests
# import re


# url = "https://a1trading.com/market-analysis/cot/"
# result = requests.get(url).text
# doc = BeautifulSoup(result, "html.parser")

# # react_tag = doc.find_all(["rect"])
# # rect_tag = doc.tbody

# body = doc.body

# print(body)






