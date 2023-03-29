from bs4 import BeautifulSoup
import requests
import random


# --------------------------------------------
# --------------------------------------------
#      Using Proxy Pool to Send Request
# --------------------------------------------
# --------------------------------------------


# Using Proxy Pool to avoid IP Ban
# Free Proxies used from: https://www.sslproxies.org/#
# Proxy Format: http://ip:port or https://ip:port

proxy_list = [
    'https://198.59.191.234:8080',
    'https://94.131.114.69:3128',
    'https://8.219.97.248:80',
    'https://20.191.183.134:3129',
    'https://130.41.109.158:8080',
    'https://210.148.141.4:8080',
    'https://135.181.114.87:33820',
    'https://82.146.48.200:8000',
    'https://20.191.183.56:3129',   
]
# proxy_list = [
#     'http://103.142.141.71:80',
# ]


proxy = random.choice(proxy_list)

proxies = {
    'http': proxy,
    'https': proxy
}

url = "https://ikman.lk/en/ads/"


result = requests.get(url, proxies=proxies, verify=False, allow_redirects=True).text
doc = BeautifulSoup(result, "html.parser")

print(doc)


# --------------------------------------------
# --------------------------------------------
# There is an error with the proxy server
# --------------------------------------------
# --------------------------------------------


# url = "https://tradingeconomics.com/european-union/gdp-annual-growth-rate"
# result = requests.get(url).text
# doc = BeautifulSoup(result, "html.parser")

# tbody = doc.tbody
# print(doc)



# https://www.zenrows.com/blog/user-agent-web-scraping#2-keep-random-intervals-between-requests




