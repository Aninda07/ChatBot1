import requests

url = "https://aiubanik.pagekite.me/2"

payload={}
headers = {
  'Authorization': 'Basic QW5pbmRhIEFuaWs6WnhjMTIzIT8='
}

response = requests.request("GET", url, headers=headers, data=payload)


r1 = response.json()

Q1 = r1[0]["web_url_1"]

print(Q1)