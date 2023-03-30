import requests
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')

# Documentation: https://www.alphavantage.co/documentation/

url = 'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey=api_key'
r = requests.get(url)
data = r.json()

print(data)
