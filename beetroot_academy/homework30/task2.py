# Task 2
# Load data
# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.

import requests
import json


URL = 'https://api.pushshift.io/reddit/comment/search/'
response = requests.get(URL)
resp_jason = response.json()
content = {'data':[]}
for i in resp_jason['data']:
    author = i['author']
    body = i['body']
    content['data'].append({"Author":author,"Comment":body})

print(content)


with open('comments.json', 'w') as file:
    json.dump(content,file,indent=4)
    file.close()







