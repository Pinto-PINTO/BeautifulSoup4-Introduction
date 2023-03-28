from bs4 import BeautifulSoup
import requests
import re


url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")


tbody = doc.tbody
trows = tbody.contents

names_and_prices = {}
first_set = {}
second_set = {}


# First 10 Crypto Currencies
for tr in trows[:10]:
    name, price = tr.contents[2:4]
    # print(name.p.string)
    # print(price.span.string)
    # print()
    first_names_set = name.p.string
    first_prices_set = price.span.string
    first_set[first_names_set] = first_prices_set


# Atfer first 10 
for tr in trows[10:]:
    name, price = tr.contents[2:4]
    # print(name.a.contents[1].string)
    # print(price.span.contents[0] + price.span.contents[2])   # Concatinating $ with price.  [0] -> $ sign   [2] -> contains the price
    # print()
    second_names_set = name.a.contents[1].string
    second_prices_set = price.span.contents[0] + price.span.contents[2]
    second_set[second_names_set] = second_prices_set



# Merge Dictonaries
names_and_prices = first_set | second_set
print(names_and_prices)

