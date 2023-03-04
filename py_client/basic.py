import requests

# endpoint = "https://www.httpbin.org/anything"


# response = requests.get(endpoint, json={"query": "Hello World"})

endpoint  = "http://localhost:8000/api/restapi/"
response = requests.get(endpoint, params={"abc": 2, "name": "shankar"}, json={"Query": "Hello"})
print(response.text)
print(response.json())
# We can also get status code whether that endpoint is there in the server or not
print(response.status_code)