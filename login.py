import requests
url = ""

data = {
    "userId": "",
    "password":  "",
    "service": "",
    "queryString":"",
    "passwordEncrypt": "true"
}

header = {
    "Accept": "*/*",
    "Accept-Encoding": "",
    "Accept-Language": "",
    "Connection": "",
    "Content-Length": "",
    "Content-Type": "",
    "Cookie": " ",
    "Host": "",
    "Origin": "",
    "Referer": "",
    "User-Agent": ""
}

response=requests.post(url,data,headers=header)
response.encoding='utf8'
print(response.text)

