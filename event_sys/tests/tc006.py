import requests,pprint


payload = {
    'username': '1111111',
    'password': '123456'
}

response = requests.post('http://127.0.0.1:8000/api/my_space/I_ve_joined?action=listevent&id=11111111')

pprint.pprint(response.json())