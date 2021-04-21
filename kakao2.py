import requests
import json
import sys
# x_auth_token: 33c9ae0a0e9a16ed5641bae34e20b739
BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
headers = {'Content-type': 'application/json', 'X-Auth-Token': '33c9ae0a0e9a16ed5641bae34e20b739'}
req = requests.post(BASE_URL + "/start", headers=headers, params={'problem': 1})
auth_key = json.loads(req.text)['auth_key']

Location_headers = {'Content-type': 'application/json', 'Authorization': auth_key}
Location_req = requests.get(BASE_URL + "/locations", headers=Location_headers)
Truck_req = requests.get(BASE_URL + "/trucks", headers=Location_headers)
print(Location_req.text)
print(Truck_req.text)


data = {"commands": [{"truck_id": 0, "command": [2, 5, 4, 1, 6]}]}
# for i in range(720):
#     Simulate_req = requests.put(BASE_URL + "/simulate", headers=Location_headers,
#                                 data=json.dumps(data))
#     print(Simulate_req)



Score_req = requests.get(BASE_URL + "/score", headers=Location_headers)
print(Score_req.text)
