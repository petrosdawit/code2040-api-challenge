# author: Petros Dawit
# email: petros_dawit@brown.edu

import json, requests

class Code2040(object):

	def __init__(self):
		url = 'http://challenge.code2040.org/api/register'
		api_token = 'a4fc745af73d19fc0356b3cc4b9f1243'
		github_url = 'https://github.com/petrosdawit/code2040-api-challenge'
		payload = json.dumps({'token' : api_token, 'github' : github_url})

		r = requests.post(url, params = payload)	
		print r.url

if __name__ == '__main__':
	code2040 = Code2040()

