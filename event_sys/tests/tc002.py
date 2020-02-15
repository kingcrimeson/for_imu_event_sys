import  requests,pprint

url ='http://127.0.0.1:8000/api/index?action=listevent'
headers = {
    'session' :'NDNlYTkyZGM2MDU5NDFkNzE1NjYyMzY3ODUzMmVjMWRlZjQyNWQyMzp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiIxMTExMTExMSIsInBlcm1pc3Npb24iOm51bGx9'
}
response = requests.get(url=url,headers=headers)
pprint.pprint(response.json())