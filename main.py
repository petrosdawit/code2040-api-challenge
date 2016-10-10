# author: Petros Dawit
# email: petros_dawit@brown.edu

import json, requests

url = 'http://challenge.code2040.org/api/register'
api_token = 'a4fc745af73d19fc0356b3cc4b9f1243'
github_url = 'https://github.com/petrosdawit/code2040-api-challenge'
info = json.dumps({'token' : api_token, 'github' : github_url})

req = requests.post(url, api_token, github_url)
print req.url
