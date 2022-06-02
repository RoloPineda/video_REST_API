import requests

BASE = "http://127.0.0.1:5000/"

data = [{'likes': 13131, 'name': 'Jen', 'views': 1000}, {'likes': 10, 'name': 'tim', 'views': 1000},
        {'likes': 10213, 'name': 'My API', 'views': 20000},
        {'likes': 10, 'name': 'Last vid', 'views': 1000}]
"""
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i),data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/12")
print(response.json())
"""

response = requests.patch(BASE + "video/2", {"views": 123, "likes": 200})
print(response.json())
