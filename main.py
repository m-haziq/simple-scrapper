import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = 'http://teamcreek.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")


all_links = soup.findAll('a')
for link in all_links:
	print(link)


