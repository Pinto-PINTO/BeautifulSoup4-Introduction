from bs4 import BeautifulSoup
import requests
import re

url = "https://www.myfxbook.com/community/outlook"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")


tbody = doc.find(["tbody"], id="outlookSymbolsTableContent")
trow = doc.find_all(["tr"], class_="outlook-symbol-row")


forex_sentiment = []

# -------------------------------------------
# Important Extracing Attributes of a Tag
# -------------------------------------------

# Extracting 79% from style in:  <div class="progress-bar progress-bar-danger" style="width: 79%;"></div>

# Regular Expressions, r'width:\s*(\d+%);'
# 1)   "width:" - a literal string that matches the characters "width:".
# 2)   \s*      - zero or more whitespace characters (spaces, tabs, or newlines).
# 3)   (\d+%);  - a capturing group that matches the following:
#   i) \d+%     - a string of one or more digits, followed by a percent symbol ("%").
#  ii) ;        - a literal semicolon.


# Regular Epression pattern is used to search for a string that has a width property defined in CSS syntax, 
# followed by a percentage value (with the % symbol), and then terminated by a semicolon.

# For example, it would match strings like:
#    i) width: 20%;
#   ii) width: 50%; margin-left: 10px;
#  iii) width:80%;height:100px;

# -------------------------------------------
# -------------------------------------------
# -------------------------------------------


# Dont use variables a1, a2, ...
for tr in trow[:4]:
    symbol, a1, percentage, a2, popularity, a3, short_price_and_pips, a4, long_price_and_pips, a5, current_price = tr.contents[1:12]
    
    symbol_value = symbol.a.string.lstrip()     # Removing space in front
    
    shorts_trend_div_tag = percentage.find(["div"], class_="progress-bar-danger")    # Entire div
    shorts_trend_style_content = shorts_trend_div_tag.get('style')   # Value inside the style which is width: 77%
    shorts_trend_value = re.search(r'width:\s*(\d+%);',  shorts_trend_style_content).group(1)   # Get exact width value using regular expression
    
    longs_trend_div_tag = percentage.find(["div"], class_="progress-bar-success")    
    longs_trend_style_content = longs_trend_div_tag.get('style')   
    longs_trend_value = re.search(r'width:\s*(\d+%);',  longs_trend_style_content).group(1)   
    
    popularity_div_tag = popularity.find(["div"], class_="progress-bar")
    popularity_style_content = popularity_div_tag.get('style')   
    popularity_value = re.search(r'width:\s*(\d+%);',  popularity_style_content).group(1)   
    
    record = {}
    record["symbol"] = symbol_value
    record["short_trend"] = shorts_trend_value
    record["long_trend"] = longs_trend_value
    record["popularity"] = popularity_value
    
    
    
    forex_sentiment.append(record)
    
    # print(popularity_value)
    # print(short_price_and_pips)
    # print(long_price_and_pips)
    # print(current_price)
    # print()


print(forex_sentiment)