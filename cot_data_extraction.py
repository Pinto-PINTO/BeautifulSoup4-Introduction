from bs4 import BeautifulSoup
import requests
import re

url = "https://www.cftc.gov/dea/futures/deacmesf.htm"
# url = "https://a1trading.com/market-analysis/cot/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

pre_tag = doc.pre
pre_tag_data = pre_tag.text.strip()


# search_string = "CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE"

# if search_string in pre_tag_data:
#     print("Found")

# else:
#     print("Not Found")


# print(pre_tag_data)

# value_1 = pre_tag_data[505:512].strip()  # "18,812"
# value_2 = pre_tag_data[513:520].strip()  # "75,633"

# print(value_1, value_2)  # output: "18,812 75,633"

# pattern = r"USD Malaysian Crude Palm Oil C - CHICAGO MERCANTILE EXCHANGE\s+Code-037021\s+FUTURES ONLY POSITIONS AS OF \d{2}/\d{2}/\d{2}\s+\|\s+[-]+\|\s+NONREPORTABLE\s+[\s\S]*?COMMITMENTS\s+([\d,]+)\s+([\d,]+)"
pattern = r"BUTTER (CASH SETTLED) - CHICAGO MERCANTILE EXCHANGE\s+050642\s+FUTURES ONLY POSITIONS AS OF \d{2}/\d{2}/\d{2}\s+\|\s+[-]+\|\s+NONREPORTABLE\s+[\s\S]*?COMMITMENTS\s+([\d,]+)\s+([\d,]+)"
match = re.search(pattern, pre_tag_data)

if match:
    value1 = match.group(1).replace(",", "")
    value2 = match.group(2).replace(",", "")
    print("Values found:", value1, value2)
else:
    print("Values not found")