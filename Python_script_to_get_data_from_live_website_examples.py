import requests

r = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=ff7759809f2f4a968927d6f71545ab91')
content = r.json()
print(content['articles'][0]['title'])


#https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=ff7759809f2f4a968927d6f71545ab91