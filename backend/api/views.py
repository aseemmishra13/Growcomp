from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
import requests
import re
import json
# Create your views here.


@api_view(['GET'])

def getRoutes(request):
    routes=[ {'Endpoint':'/search/amazon','method':'GET','body':None,'description':'Returns Amazon search resu;t'},
             {'Endpoint':'/search/wallmart','method':'GET','body':None,'description':'Returns Wallmart search resu;t'},
             {'Endpoint':'/search/harris','method':'GET','body':None,'description':'Returns Wallmart search resu;t'},
             {'Endpoint':'/search/target','method':'GET','body':None,'description':'Returns Wallmart search resu;t'}
            
            
            
            ]
    return Response(routes)
@api_view(['GET'])

def getResultWalmart(request,pk):


    search=pk
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
    
        
        
        if(count>len(price) or count>len(image) or count==10):
            break

        string = price[i].text
        decimal_pattern = re.compile(r'\d+\.\d+')

        matches = re.findall(decimal_pattern, string)

        if len(matches) > 0:
            decimal_value = float(matches[0])
              
            
        list1.append({'id':i,'title':titles[i].text,'price':decimal_value,'company':'walmart','image':image[i]['src']} )
        list1= sorted(list1, key=lambda x: float(x['price']))
 
 
    return Response(list1)

@api_view(['GET'])
def getResultAmazon(request,pk):
    search=pk
    URL='https://www.amazon.com/s?k='+search+'&i=amazonfresh&crid=22FD2RIOJNRR1&sprefix='+search+'%2Camazonfresh%2C106&ref=nb_sb_noss_2'


    headers=({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0','Accept-Language': 'en-US, en;q=0.5'})

    webpage=requests.get(URL,headers=headers)

    soup=BeautifulSoup(webpage.content,"html.parser")

    titles = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

    count=0

    price= soup.find_all("span", attrs={'class':'a-offscreen'})
    rating = soup.find_all("a", attrs={'class':'a-popover-trigger a-declarative'})
    image=soup.find_all("img", attrs={'class':'s-image'})
    list1=[]
    for i in range(0,len(titles)):
        count+=1
        print(titles[i].text)
        
        
        string = price[i].text
        decimal_pattern = re.compile(r'\d+\.\d+')

        matches = re.findall(decimal_pattern, string)

        if len(matches) > 0:
            decimal_value = float(matches[0])    
        if(count==10):
            break    
        
        if(count<=len(price)):
            print(rating[i].text)
            print(price[i].text)
        
            list1.append({'id':i,'title':titles[i].text,'price':decimal_value ,'company':'amazon','image':image[i]['src']} )
            list1= sorted(list1, key=lambda x: float(x['price']))
        
    return Response(list1)



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


@api_view(['GET'])
def getResultHarris(request,pk):
    search=pk
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
            string = prices[i].text
            decimal_pattern = re.compile(r'\d+\.\d+')

            matches = re.findall(decimal_pattern, string)

            if len(matches) > 0:
                decimal_value = float(matches[0])
        
            list1.append({'id':i,'title':titles[i].text,'price':decimal_value,'company':'harris', 'image': image[i]['src']} )
            list1= sorted(list1, key=lambda x: float(x['price']))
                
        

    return Response(list1) 


@api_view(['GET'])
def getResultTarget(request,pk):
   
    params = {
    'api_key': '80D36B86646A47F3ADAC35C5D8C0F7CE',
    'search_term': pk,

    'type': 'search'
    }

    # make the http GET request to RedCircle API
    api_result = requests.get('https://api.redcircleapi.com/request', params)

    # print the JSON response from RedCircle API
    lis1=[]
    dict1={}
    count=0
    id=''
    title=''
    price=''
    for i in api_result.json():
        print(i)
        if(i!= 'search_results'):
                continue
        for j in api_result.json()[i] :
            
            for key, items in j.items():
                if(key=='position'):
                    id=j[key]
                if(key=='offers'):
                    for key1,items1 in j[key].items():
                        if(key1=='primary'):
                                price= j[key][key1]['price']
                    
                        
                if(key=='product'):
                    for key1,items1 in j[key].items():
                            if(key1=='title'):
                                
                                title=j[key][key1]
                            if(key1=='main_image'):
                             image=j[key][key1]    
            count+=1 
            lis1.append({'id':id,'price':float(price),'title':title,'company':'target','image':image})  
            lis1= sorted(lis1, key=lambda x: float(x['price']))
            if(count==10):
                break              
            

    return Response(lis1)
        


