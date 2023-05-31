import csv 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as Bs
import pandas as Pd

planetUrl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(planetUrl)
time.sleep(1)
exoplanets = []

names = []
radius = []
mass = []
distance = []

def scrapeExoPlanets():
    for i in range(0,10):
        soup = Bs(browser.page_source,"html.parser")
        tables = soup.find_all("table")
        table_rows = tables[7].find_all("tr")
        save = []
        for trtags in table_rows:
            tdtags = trtags.find_all("td")
            row = [i.text.rstrip() for i in tdtags]
            save.append(row)
        for i in range(1,len(save)):
            names.append(save[i][0])
            radius.append(save[i][5])
            mass.append(save[i][7])
            distance.append(save[i][8])
    df2 = Pd.DataFrame(list(zip(names,radius,mass,distance)),columns=["name","radius","mass","distance"])
    print(df2)
    df2.to_csv("hw128")
scrapeExoPlanets()
print(mass)