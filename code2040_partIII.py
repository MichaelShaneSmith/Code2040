import requests
import json

urls = {
	'get_resources' : 'http://challenge.code2040.org/api/haystack',
	'validate' : 'http://challenge.code2040.org/api/haystack/validate'
}

# Setup
params1 = {
	'token' : '<token>'
}
response1 = requests.post(urls['get_resources'], data=params1)

# Find Index
resource_dict = response1.json()
needle = resource_dict['needle']
haystack = resource_dict['haystack']
ans = haystack.index(needle)

# Return Answer
params2 = {
	'token' : '<token>',
	'needle' : ans	
}
response2 = requests.post(urls['validate'], data=params2)
print response2.text