from bs4 import BeautifulSoup
import requests
import re


# Passing url using Beautiful soup Html parser and getting the document
url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")




# --------------------------------------------------
# --------------------------------------------------
# Example Tree Structure:
# <table> 
#     <thead>
#         <tr> 
#             <th> </th>   # Siblings 1
#             <th> </th>   # Siblings 1
#             <th> </th>   # Siblings 1
#         </tr>
#     </thead>

#     <tbody>
#         <tr> </tr>    # Siblings 2
#         <tr> </tr>    # Siblings 2
#         <tr> </tr>    # Siblings 2
#         <tr> </tr>    # Siblings 2
#     </tbody>
# </table>

# Here: 
# -> Parent of <tr> is <tbody>
# -> Parent of <th> is <tr>
# -> Parent of <tr> is <thead>
# -> Parent of both <thead> and <tbody> is <table>
# -> <thead> and <tbody> are siblings
# -> Siblings means they are in the same hierarchical level

# --------------------------------------------------
# --------------------------------------------------


# 1 - Tree Siblings
# Getting all table rows which is inside table body
# table_body = doc.tbody
# table_rows = table_body.contents


# 1.1 - Prints all table rows
# print(table_rows)  

# 1.2 - Prints the first table row (BTC)
# print(table_rows[0])

# 1.3 - Prints the next table row (ETH)
# print(table_rows[0].next_sibling) 

# 1.4 - Prints the previous table row (BTC)
# print(table_rows[1].previous_sibling) 

# 1.5 - All the rows that come after the first table row
# print(list(table_rows[0].next_siblings))




# 2 - Parents and Descends
# 2.1 - Give the entire parent (Entire tbody tag)
# print(table_rows[0].parent)

# 2.2 - Give the parent name (tbody)
# print(table_rows[0].parent.name)

# 2.3 - Prints the all the children (contents) inside the tag
# Contents / Children 
# print(list(table_rows[1].children))
# print(list(table_rows[0].contents))




# 3 - Getting Crypto Prices for first 10 

table_body = doc.tbody
table_rows = table_body.contents

names_and_price = {}

# 3.1 - Interate the content inside the <tr> tag
# for tr in table_rows:
#     print(tr)
#     print()


# 3.2 - Interate the content inside the <td> tag
# for tr in table_rows:
#     for td in tr.contents[2:4]:     # Print only the second and forth (Getting name and price only from the table)
#         print(td)
#         print()


# 3.3 - Storing the name and price into 2 variables
# looking at only the first 10 table rows
# for tr in table_rows[:10]:
#     name, price = tr.contents[2:4] 
#     print(name.p.string)   # The name that we want is inside the <p> tag 
#     print()


# 3.4 - Final Code
for tr in table_rows[:10]:
    name, price = tr.contents[2:4]   # Content in 2nd column goes to name, Content in 4th column goes to price
    cryto_names = name.p.string
    crypto_prices = price.span.string
    
    names_and_price[cryto_names] = crypto_prices   # Populating both names and prices into the dictionary


print(names_and_price)

