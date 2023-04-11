from bs4 import BeautifulSoup
import requests
import pandas as pd

URL='https://www.amazon.com/s?k=tomato&crid=6CZE1DZS5F9J&sprefix=tomato%2Caps%2C223&ref=nb_sb_noss_1'


headers=({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0','Accept-Language': 'en-US, en;q=0.5'})

webpage=requests.get(URL,headers=headers)

soup=BeautifulSoup(webpage.content,"html.parser")

links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

links_list = []
for link in links:
            links_list.append(link.get('href'))
d = {"title":[], "price":[]}


for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=headers)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        title=new_soup.find("span", attrs={"id":'productTitle'}).text.strip()
        print(title)
        try:
            price=new_soup.find("span", attrs={"class":'a-price a-text-price a-size-medium apexPriceToPay'}).find("span", attrs={"class": "a-offscreen"}).text
        except:
            price = ""    
        print(price)