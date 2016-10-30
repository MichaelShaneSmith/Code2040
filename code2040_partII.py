import requests

urls = {
	'reverse' : 'http://challenge.code2040.org/api/reverse',
	'validate' : 'http://challenge.code2040.org/api/reverse/validate'
}

# Setup
params1 = {
	'token' : '<token>'
}
response1 = requests.post(urls['reverse'], data=params1)

# Reverse word
word = response1.text
ans = word[::-1]
# ^^ This is like saying, 'give me the letters of the string in steps of one 
# but backwards from the end to the beginning'

# Return Answer
params2 = {
	'token' : '<token>',
	'string' : ans	
}
response2 = requests.post(urls['validate'], data=params2)
print response2.text