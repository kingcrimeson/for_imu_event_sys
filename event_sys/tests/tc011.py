import  requests,pprint
dat = {
"action" : 'delete',
            "event_id" : 4
}
response = requests.delete('http://127.0.0.1:8000/api/mgr/delete',json=dat)

pprint.pprint(response.json())