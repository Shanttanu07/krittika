import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from time import sleep

pd.set_option('display.max_colwidth', 255)

database=[]
year=[2019,2020,2021,2022]

for i in year:
    team=[]
    url='https://krittikaiitb.github.io/team/'
    request_content=requests.get(url).content
    soup=BeautifulSoup(request_content,'html.parser')

    name=soup.select(('#team-{} h5').format(i))
    desig=soup.select(('#team-{} .card-text').format(i))
    for p in range(len(name)):
        member={"Name": None, "Designation": None}
        member['Name']=name[p].text
        member['Designation']=desig[p].text
        team.append(member)
    database.append(team)

for k in database:
    print(k)

# with open('kritika_database.json', 'w') as f:
#     json.dump(database, f)
#     f.close()

# with open('kritika_database.json', 'r') as f:
#     data = json.load(f)

# df=pd.read_json(open('kritika_database.json','r'))
# # df.head(15)
# # df.tail(15)
# print(df.head(10))
