import requests
import json

urls = {
	'get_resources' : 'http://challenge.code2040.org/api/prefix',
	'validate' : 'http://challenge.code2040.org/api/prefix/validate'
}

# Setup
params1 = {
	'token' : '<token>'
}
response1 = requests.post(urls['get_resources'], data=params1)

# Filter Array
resource_dict = response1.json()
prefix = resource_dict['prefix']
array = resource_dict['array']

ans = []
for i in range(len(array)):
	if prefix not in array[i]:
		ans.append(array[i])

# Return Answer
params2 = {
	'token' : '<token>',
	'array' : ans
}
response2 = requests.post(urls['validate'], json=params2)
print response2.text

# Please see the README for more comments on this stage