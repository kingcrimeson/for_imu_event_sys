import  requests,pprint
dat = {
"action" : 'power_give',
            "username" : '12345678'
}
response = requests.post('http://127.0.0.1:8000/api/mgr/power_give',json=dat)

pprint.pprint(response.json())