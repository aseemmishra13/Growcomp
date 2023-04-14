from bs4 import BeautifulSoup
import requests
import pandas as pd

search='bread'
URL='https://www.amazon.com/s?k='+search+'&i=amazonfresh&crid=22FD2RIOJNRR1&sprefix='+search+'%2Camazonfresh%2C106&ref=nb_sb_noss_2'
print(URL)

headers=({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0','Accept-Language': 'en-US, en;q=0.5'})

webpage=requests.get(URL,headers=headers)

soup=BeautifulSoup(webpage.content,"html.parser")
print(soup)
titles = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

count=0

price= soup.find_all("span", attrs={'class':'a-offscreen'})
rating = soup.find_all("a", attrs={'class':'a-popover-trigger a-declarative'})
image=soup.find_all("img", attrs={'class':'s-image'})
list1=[]
for i in range(0,len(titles)):
    count+=1
    print(titles[i].text)
    print(price[i].text)
   
    
    
    if(count<=len(rating)):
        print(rating[i].text)
        print(image[i]['src'])
       
        list1.append({'id':i,'title':titles[i].text,'price':price[i].text,'image':image[i]['src']} )

print(list1)