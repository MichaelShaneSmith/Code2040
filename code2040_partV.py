import requests
import datetime

urls = {
	'get_resources' : 'http://challenge.code2040.org/api/dating',
	'validate' : 'http://challenge.code2040.org/api/dating/validate'
}

# Setup
params1 = {
	'token' : '<token>'
}
response1 = requests.post(urls['get_resources'], data=params1)
resource_dict = response1.json()

# Add Seconds
## Parse the datetime with the pattern found fron looking at the inputs
date = datetime.datetime.strptime(resource_dict['datestamp'], 
								  r'%Y-%m-%dT%H:%M:%SZ')
delta = resource_dict['interval']
newtime = date + datetime.timedelta(seconds=delta)
## Create a properly formatted string using the same pattern from above
ans_str = newtime.strftime(r'%Y-%m-%dT%H:%M:%SZ')

# Return Answer
params2 = {
	'token' : '<token>',
	'datestamp' : ans_str
}
response2 = requests.post(urls['validate'], data=params2)
print response2.text