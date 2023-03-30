from bs4 import BeautifulSoup
import requests
import re

# url = "https://www.cftc.gov/dea/futures/deacmesf.htm"
url = "https://a1trading.com/market-analysis/cot/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

print(doc)