# author: Petros Dawit
# email: petros_dawit@brown.edu

from json import dumps, loads
from urllib2 import urlopen, Request

api_token = 'a4fc745af73d19fc0356b3cc4b9f1243'
github_url = 'https://github.com/petrosdawit/code2040-api-challenge'

req = Request('http://challenge.code2040.org/api/register', api_token, github_url)