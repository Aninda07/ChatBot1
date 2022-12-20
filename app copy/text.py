import requests

def send(msg,id):
    import json

    url = "https://aiubanik.pagekite.me/1"

    payload = json.dumps({
        "Chat_Received": msg,
        "Response": "text",
        "Sender_ID": id,
    })
    headers = {
  'Authorization': 'Basic QW5pbmRhIEFuaWs6WnhjMTIzIT8='
}
    respons = requests.request("POST", url, headers=headers, data=payload)