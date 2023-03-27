from bs4 import BeautifulSoup
import requests


url = 'https://www.newegg.com/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771?Item=N82E16814137771'


# 1 - Read any HTML Website
# Makes an HTTP Get request and stores the data in the result variable
result = requests.get(url)
# print(result.text)


# 2 - Getting the HTML document from BeautifulSoup
doc = BeautifulSoup(result.text, "html.parser") 
# print(doc.prettify())


# 3 - Find the price using the Dollar Sign "$" indicated in the price in the website
prices = doc.find_all(text="$")
print(prices)


# 4 - Finding the parent of the first Dollar Sign 
# The parent holds the dollar sign: eg: <h1> <p> $ 200 </p> </h1>
# The parent of $200 is the "p" tag. The parent of the "p" tag is the "h1" tag
parent = prices[0].parent
# print(parent)


# 5 - Finding the strong tag to extract the price in string
strong = parent.find("strong")
print(strong.string)


















