#Example 1: Search worldwide news with code:
#Documentation : https://newsapi.org/docs

import requests

r = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=<api-key>')
content = r.json()
print(content['articles'][0]['title'])


#https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=<api-key>
