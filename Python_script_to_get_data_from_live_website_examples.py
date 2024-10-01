#Example 1: Search worldwide news with code:
#Documentation : https://newsapi.org/docs
#Accessing API and working with json data

import requests

r = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=<api-key>')
content = r.json()
print(content['articles'][0]['title']) 


#https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=<api-key>
