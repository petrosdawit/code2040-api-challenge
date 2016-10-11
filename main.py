# author: Petros Dawit
# email: petros_dawit@brown.edu

import json, requests
from StringIO import StringIO

class Code2040(object):

	def __init__(self):
		self._headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
		self._api_token = 'a4fc745af73d19fc0356b3cc4b9f1243'

		url = 'http://challenge.code2040.org/api/register'
		github_url = 'https://github.com/petrosdawit/code2040-api-challenge'
		payload = {'token' : self._api_token, 'github' : github_url}
		r = requests.post(url, data = json.dumps(payload), headers = self._headers)
		print r.text

	def step2(self):
		reverse_url = 'http://challenge.code2040.org/api/reverse'
		payload = {'token' : self._api_token}
		r = requests.post(reverse_url, data = json.dumps(payload), headers = self._headers)
		
		#reversing the string
		string = r.text
		reversed_string = string[::-1]

		validate_url = 'http://challenge.code2040.org/api/reverse/validate' 
		payload = {'token' : self._api_token, 'string' : reversed_string}
		r = requests.post(validate_url, data = json.dumps(payload), headers = self._headers)
		print r.text

	def step3(self):
		haystack_url = 'http://challenge.code2040.org/api/haystack'
		payload = {'token' : self._api_token}
		r = requests.post(haystack_url, data = json.dumps(payload), headers = self._headers)

		#loading json
		data = json.loads(r.text)
		needle = data['needle']
		haystack = data['haystack']

		#looping through the haystack and looking for the needle
		n = len(haystack)
		index = 0
		for i in range(n):
			if needle == haystack[i]:
				index = i

		validate_url = 'http://challenge.code2040.org/api/haystack/validate'
		payload = {'token' : self._api_token, 'needle' : index}
		r = requests.post(validate_url, data = json.dumps(payload), headers = self._headers)
		print r.text

	def step4(self):
		prefix_url = 'http://challenge.code2040.org/api/prefix'
		payload = {'token' : self._api_token}
		r = requests.post(prefix_url, data = json.dumps(payload), headers = self._headers)

		data = json.loads(r.text)
		prefix = data['prefix']
		array = data['array']

		result_array = []
		n = len(array)
		for i in range(n):
			if not array[i].startswith(prefix):
				result_array.append(array[i])

		headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

		validate_url = 'http://challenge.code2040.org/api/prefix/validate'
		payload = {'token' : self._api_token, 'array' : result_array}
		r = requests.post(validate_url, data = json.dumps(payload), headers = self._headers)
		print r.text


if __name__ == '__main__':
	code2040 = Code2040()
	code2040.step2()
	code2040.step3()
	code2040.step4()


