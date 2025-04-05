import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
username = "dagimmengestu5"
token = "dagimmengestu5@gmail.com"
graphs_id = "graph1"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = { "X-USER-TOKEN":token}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixle_create_endpoint = f"{graph_endpoint}/{username}/graphs/graph1"
today = datetime.now()
pixle_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6"
}
response = requests.post(url=pixle_create_endpoint, json=pixle_data, headers=headers)

update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphs_id}/{today.strftime("%Y%m%d")}"

new_pixle_data = {
    "quantity": "20"
}
response = requests.put(url=update_endpoint, json=new_pixle_data, headers=headers)
print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphs_id}/{today.strftime("%Y%m%d")}"