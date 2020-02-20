import requests,pprint


payload = {
    'username': '11111111',
    'password': '123456'
}

response = requests.post('http://127.0.0.1:8000/api/login',data=payload)

pprint.pprint(response.json())