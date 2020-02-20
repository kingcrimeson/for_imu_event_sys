import  requests,pprint

payload = {
        "action" : "register",
        "data": {
    "username" :"12345678",
"nichen": "键健",
"password1": "123456",
"password2": "123456",
"email": "11111221@qq.com"
}
}


response = requests.post('http://127.0.0.1:8000/api/register',
              json=payload)

pprint.pprint(response.json())