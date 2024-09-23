import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import numpy as np
import csv
import matplotlib.pyplot as plt
import os
import pandas as pd

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.ruparupa.com/c/rak-dan-penyimpanan/rak/rak-buku.html?itm_source=megamenu-rak-buku&itm_campaign=third-level&itm_device=desktop"

driver.get(url)

time.sleep(5)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')

links = []
itemlink = soup.find_all('div', class_='row product-card')
for link in itemlink:
    for item in link.find_all('a', href=True):
        links.append(item['href'])
        print(item['href'])

AjazzList = []
products = soup.find_all('div', class_='container-card__product container-card__product--mobile')
for product in products:
    a = product.find('span', class_='product__name')
    h = product.find('div', class_='price__initial')
    i = product.find('span', class_='ui-text-4 text__grey50')
    if a and h and i:
        AjazzList.append({'Nama': a.text.strip(), 'Harga': h.text.strip(), 'Rating': i.text.strip()}) 
        print(AjazzList)
            
df = pd.DataFrame(AjazzList, columns=['Nama','Harga','Rating'])
print(df)
directory = r'D:\coding\PYTHON\TIK KELAS 12'
filename = "Data-Rak.csv"
file_path = os.path.join(directory, filename)

df.to_csv(file_path, index=False)

print(f"File saved at {file_path}")
driver.quit