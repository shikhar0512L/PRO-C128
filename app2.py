from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = ("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")

wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")
start_table = soup.find_all('table')
temp_list = []

table_row = start_table[7].find_all('tr')

for tr in table_row:
    td = tr.find_all('td')
    row =[i.text.rstrip() for i in td]
    temp_list.append(row)

Star_name = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(temp_list)):
    Star_name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

d2 = pd.DataFrame(list(zip(Star_name,Distance,Mass,Radius)),columns=["Star_name","Distance","Mass","Radius"])
d2.to_csv("data2.csv")