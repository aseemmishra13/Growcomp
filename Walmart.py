from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

search='pringle'
URL='https://www.walmart.com/search?q='+search+'&catId=976759'


headers=({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0','Accept-Language': 'en-US, en;q=0.5'})

webpage=requests.get(URL,headers=headers)
print(webpage)
soup=BeautifulSoup(webpage.content,"html.parser")

count=0
titles = soup.find_all("span", attrs={'class':'w_V_DM'})
price= soup.find_all("div", attrs={'data-automation-id':'product-price'})
rating = soup.find_all("div", attrs={'class':'flex items-center mt2'})
image= soup.find_all("img", attrs={'data-testid':'productTileImage'})

list1=[]
for i in range(0,len(titles)):
    count+=1
    print(titles[i].text)
    
   
    
    
    if(count<=len(image)):
        print(rating[i].text[2:])
        print(price[i].text)
        print(image[i]['src'])
        list1.append({'id':i,'title':titles[i].text,'price':price[i].text,'image':image[i]['src']} )

print(list1)          
json_output = json.dumps(list1)

# Print JSON output
print(json_output)
 