#### WEB SCRAPPING ####

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# time.sleep(random.uniform(1.5, 3.5))

response = requests.get('https://www.ambitionbox.com/list-of-companies?page=1')
print(response)
print(response.text) # don't have a permission to access and hence the request is being rejected

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'Accept-Language' : 'en-US,en;q=0.9',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}

name = []
rating = []
votes = []
salary = []
location = []
sector = []

for i in range(1,30): # getting data of first 29 pages
    response = requests.get('https://www.ambitionbox.com/list-of-companies?page={}'.format(i), headers=headers)
    webpage = response.text
    soup = BeautifulSoup(webpage, 'lxml')
    # print(soup.prettify())
    company = soup.find_all('div', class_="companyCardWrapper")

    print(i)

    for i in company:
        name.append(i.find('h2').text.strip())

        rating.append(i.find('div', class_='rating_text').text.strip())

        votes.append(i.find_all('a', class_ = 'companyCardWrapper__ActionWrapper')[0].find('span', class_="companyCardWrapper__ActionCount").text.strip())
        
        salary.append(i.find_all('a', class_ = 'companyCardWrapper__ActionWrapper')[1].find('span', class_="companyCardWrapper__ActionCount").text.strip())

        sector.append(i.find('span', class_='companyCardWrapper__interLinking').text.strip().split('|')[0])

        location.append(i.find('span', class_='companyCardWrapper__interLinking').text.strip().split('|')[1].split()[0])


d = {
    'name' : name,
    'rating' : rating,
    'votes' : votes,
    'salary' : salary,
    'sectors' : sector,
    'location' : location
}
df = pd.DataFrame(d)
df.to_csv('created_scraped_data.csv', index=False)
