from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrap(search):
    URL='https://www.harristeeter.com/search?query='+search+'&searchType=default_search'


    headers=({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0','Accept-Language': 'en-US, en;q=0.5'})

    webpage=requests.get(URL,headers=headers)
    print(webpage)
    soup=BeautifulSoup(webpage.content,"html.parser")



    titles=soup.find_all('h3',attrs={'data-qa':'cart-page-item-description'})
    prices=soup.find_all('mark',attrs={'class':'kds-Price-promotional kds-Price-promotional--plain kds-Price-promotional--decorated'})
    image=soup.find_all('img',attrs={'data-qa':'cart-page-item-image-loaded'})
    return titles,prices,image
search='monster'
titles,prices,image=scrap(search)
list1=[]
count=0
while(len(titles)==0):
    titles,prices,image=scrap(search)

for i in range(0,len(titles)):
    count+=1
    print(titles[i].text)
    
   
    if(count==10):
        break
    
    if(count<=len(prices)):
        print(prices[i].text)
       
        list1.append({'id':i,'title':titles[i].text,'price':prices[i].text, 'image': image[i]['src']} )
        
    

print(list1)        
