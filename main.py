# author: Petros Dawit
# email: petros_dawit@brown.edu

import json, requests
from datetime import timedelta
import dateutil.parser

class Code2040(object):

	"""	
		Here is my Code2040 class. It covers all 5 steps (registration, reverse string, needle in haystack
		prefix and dating). This coding challenge was finished in one night on Oct 10, 2016
	"""

	def __init__(self):
		#headers and api_token will be used for each method when making the http post request
		self._headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
		self._api_token = 'a4fc745af73d19fc0356b3cc4b9f1243'

		#registering
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

		#going through array and checking each string in array if it DOES NOT start with the prefix
		#if it doesn't, I append it to the result_array
		result_array = []
		n = len(array)
		for i in range(n):
			if not array[i].startswith(prefix):
				result_array.append(array[i])

		validate_url = 'http://challenge.code2040.org/api/prefix/validate'
		payload = {'token' : self._api_token, 'array' : result_array}
		r = requests.post(validate_url, data = json.dumps(payload), headers = self._headers)
		print r.text

	def step5(self):
		prefix_url = 'http://challenge.code2040.org/api/dating'
		payload = {'token' : self._api_token}
		r = requests.post(prefix_url, data = json.dumps(payload), headers = self._headers)

		data = json.loads(r.text)
		datestamp = data['datestamp']
		interval = data['interval']

		#parse through the datestamp to get a time and add to it the interval converted into seconds
		#I then get rid of the timezone and put it back to iso8061 format
		dt = dateutil.parser.parse(datestamp) + timedelta(seconds=interval)		 
		dt = dt.replace(tzinfo=None)
		dt = dt.isoformat() + 'Z'

		validate_url = 'http://challenge.code2040.org/api/dating/validate'
		payload = {'token' : self._api_token, 'datestamp' : dt}
		r = requests.post(validate_url, data = json.dumps(payload), headers = self._headers)
		print r.text

if __name__ == '__main__':
	code2040 = Code2040()
	code2040.step2()
	code2040.step3()
	code2040.step4()
	code2040.step5()


