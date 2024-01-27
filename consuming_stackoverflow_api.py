import requests
import json

# https://api.stackexchange.com/docs/questions
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# gets title of stackoverflow questions
for data in response.json()['items']:
    print(data['title'])