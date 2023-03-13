# Day 37: Habit tracker using pixe.la

import requests
import datetime

# change both to your info
USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(pixela_endpoint, json=user_params)
# response.raise_for_status()
#
# print(response.text)


## create graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "reading",
    "name": "Reading graph",
    "unit": "pages",
    "type":  "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

## add a pixel

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/reading"

today = datetime.datetime.now().strftime("%Y%m%d")

pixel_params = {
    "date": today,
    "quantity": "50",
}

# response = requests.post(pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

## Update a pixel

date = (datetime.datetime.now().date() - datetime.timedelta(days=1)).strftime("%Y%m%d")

cpixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/reading/{date}"

cpixel_params = {
    "quantity": "20"
}

response = requests.put(cpixel_endpoint, json=cpixel_params, headers=headers)
print(response.text)