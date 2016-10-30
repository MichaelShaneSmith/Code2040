import requests

url = 'http://challenge.code2040.org/api/register'

params = {
	'token' : '<token>',
	'github' : 'https://github.com/MichaelShaneSmith/Code2040'
}

response = requests.post(url, data=params)
print response.text