import  requests,pprint

data = {
    'username':'12345678',
    'oldpass':'123458',
    'password1':'123458',
    'password2':'12345'
}



response = requests.post('http://127.0.0.1:8000/api/my_space/change',json=data)
pprint.pprint(response.json())