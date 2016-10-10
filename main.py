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
		print r.text

	def step2(self):
		reverse_url = 'http://challenge.code2040.org/api/reverse'
		payload = {'token' : self._api_token}
		r = requests.post(reverse_url, data = payload)
		
		#reversing the string
		string = r.text
		reversed_string = string[::-1]

		validate_url = 'http://challenge.code2040.org/api/reverse/validate' 
		payload = {'token' : self._api_token, 'string' : reversed_string}
		r = requests.post(validate_url, data = payload)
		print r.text

	def step3(self):
		haystack_url = 'http://challenge.code2040.org/api/haystack'
		payload = {'token' : self._api_token}
		r = requests.post(haystack_url, data = payload)

		#loading json
		data = json.loads(r.text)
		needle = data['needle']
		haystack = data['haystack']

		#looping through the haystack and looking for the needle
		n = len(haystack)
		index = 0
		for i in range(len(haystack)):
			if needle == haystack[i]:
				index = i

		validate_url = 'http://challenge.code2040.org/api/haystack/validate'
		payload = {'token' : self._api_token, 'needle' : index}
		r = requests.post(validate_url, data = payload)
		print r.text

	def step4(self):
		prefix_url = 'http://challenge.code2040.org/api/prefix'
		payload = {'token' : self._api_token}
		r = requests.post(prefix_url, data = payload)

		#loading json
		data = json.loads(r.text)
		prefix = data['prefix']
		array = data['array']

		#create a new return_list. check each word in the array if it DOES NOT start with the prefix. if it
		#doesn't add it to our return list
		return_list = []
		for word in array:
			if not word.startswith(prefix):
				return_list.append(word)

		validate_url = 'http://challenge.code2040.org/api/prefix/validate'
		payload = {'token' : self._api_token, 'array' : return_list}
		r = requests.post(validate_url, data = payload)
		print r.text
		
if __name__ == '__main__':
	code2040 = Code2040()
	code2040.step2()
	code2040.step3()
	# code2040.step4()


