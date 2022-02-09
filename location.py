import requests
import json

import requests
import geoip2.database



def get_ip():
    response = requests.get("https://geolocation-db.com/json/.39.110.142.79&position=true").json()

    ip = (response['IPv4'])

    ip_adress = str(ip)

    request_url = "https://geolocation-db.com/jsonp/" + ip_adress

    response = requests.get(request_url)
    result = response.content.decode()

    result = result.split("(")[1].strip(")")

    result = json.loads(result)
    loc = (result['city'], result['state'])
    print(loc)
    return loc


# batch ip request



# response = requests.post("http://ip-api.com/batch", json=[

#     {"query": "208.80.152.201"},

#     {"query": "167.71.3.52"},

#     {"query": "206.189.198.234"},

#     {"query": "157.230.75.212"}

# ]).json()



# for ip_info in response:

#     for k,v in ip_info.items():

#         print(k,v)

#     print("\n")