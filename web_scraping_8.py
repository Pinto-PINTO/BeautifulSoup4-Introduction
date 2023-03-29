from bs4 import BeautifulSoup
import requests


# --------------------------------------------
# --------------------------------------------
#          Using Request Headers
# --------------------------------------------
# --------------------------------------------


url = "https://ikman.lk/en/ads/"

# Header used in the request (Mimic that the request was made as a real user)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Connection": "keep-alive",
#     "Upgrade-Insecure-Requests": "1",
#     "Referer": "https://www.google.com/",
#     "Cache-Control": "max-age=0",
#     "TE": "Trailers",
# }

result = requests.get(url, headers=headers).text
doc = BeautifulSoup(result, "html.parser")

print(doc)