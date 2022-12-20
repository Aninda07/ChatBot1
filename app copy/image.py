import json
import requests
def send2(msg,id):
    url = "https://aiubanik.pagekite.me/1"

    payload = json.dumps({
        "Chat_Received": msg,
        "Response": "Image Template",
        "Sender_ID": id,
    })
    headers = {
  'Authorization': 'Basic QW5pbmRhIEFuaWs6WnhjMTIzIT8='
}

    respons = requests.request("POST", url, headers=headers, data=payload)