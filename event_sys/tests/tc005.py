import  requests,pprint

payload = {
    "nichen": "阿健",
    "event":
        {
            "event_name": "啦啦啦",
            "event_start_time": "2020.3.14",
            "event_end_time": "2020.3.14",
            "event_sign_up_time": "2020.2.28",
            "event_localtion": "计算机学院212",
            "event_now_number": 0,
            "event_max_number": 10,
            "event_detail": "我们要做xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                             }

}

response = requests.post('http://127.0.0.1:8000/api/my_space/hold_event',
              json=payload)

pprint.pprint(response.json())