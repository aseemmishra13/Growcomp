import requests
import json

# set up the request parameters
search='monster'
params = {
'api_key': '80D36B86646A47F3ADAC35C5D8C0F7CE',
  'search_term': search,

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
image=''
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
        lis1.append({'id':id,'price':price,'title':title,'image':image})  
        if(count==10):
             break              
        

print(lis1)
            
                       
             
                                 