import requests

url="http://127.0.0.1:1096/api/"
req={"method":"random"}
res=requests.post(url=url,data=req)

print(res.text)