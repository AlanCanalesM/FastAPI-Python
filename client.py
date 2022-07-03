import json
import re
from urllib import response
import requests

""" 
URL = 'http://127.0.0.1:8000/api/v1/reviews'
QUERYSET = {'page':1, 'lim':2}
HEADERS = { 'accept':'application/json'}

response = requests.get(URL, headers=HEADERS, params=QUERYSET)



if response.status_code == 200:
    if response.headers.get('content-type') == 'application/json':

        reviews= response.json()

        for review in reviews:
            print(f"> score: {review['score']} - {review['review']}")

"""
"""
URL = 'http://127.0.0.1:8000/api/v1/reviews'

REVIEW = {
    'user_id':1,
    'movie_id':1,
    'review':'I almost finish this',
    'score':5
}
response = requests.post(URL, json=REVIEW)

if response.status_code == 200:
    print('Review created successfuly!')
    print(response.json()['id'])

else:
    print( response.content)}
"""
"""
REVIEW_ID = 6
URL = f"http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}"

NEW_REVIEW = {
    'review':'Review uploaded successfuly!',
    'score':5
}
response = requests.put(URL, json=NEW_REVIEW)

if response.status_code == 200:
    print('review uploaded!')
    print(response.json())

else:
    print(response.content)
"""

REVIEW_ID = 6
URL = f"http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}"

NEW_REVIEW = {
    'review':'Review uploaded successfuly!',
    'score':5
}
response = requests.delete(URL)

if response.status_code == 200:
    print('review deleted:(')
   

else:
    print(response.content)