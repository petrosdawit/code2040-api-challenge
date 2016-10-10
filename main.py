# author: Petros Dawit
# email: petros_dawit@brown.edu

import json, requests
from StringIO import StringIO

class Code2040(object):

	def __init__(self):
		url = 'http://challenge.code2040.org/api/register'
		self._api_token = 'a4fc745af73d19fc0356b3cc4b9f1243'
		github_url = 'https://github.com/petrosdawit/code2040-api-challenge'
		payload = {'token' : self._api_token, 'github' : github_url}
		r = requests.post(url, data = payload)

	def step2(self):
		reverse_url = 'http://challenge.code2040.org/api/reverse'
		payload = {'token' : self._api_token}
		r = requests.post(reverse_url, data = payload)
		
		string = r.text
		reversed_string = string[::-1]
		
		validate_url = 'http://challenge.code2040.org/api/reverse/validate' 
		payload = {'token' : self._api_token, 'string' : reversed_string}
		r = requests.post(validate_url, data = payload)

	def step3(self):
		haystack_url = http://challenge.code2040.org/api/haystack
		payload = {'token' : self._api_token}
		r = requests.post(haystack_url, data = payload)
		print r.text


if __name__ == '__main__':
	code2040 = Code2040()
	code2040.step2()
	code2040.step3()