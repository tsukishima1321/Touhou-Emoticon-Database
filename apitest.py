import requests

url="http://127.0.0.1:1096/api/"
req={"method":"getRandomUrl"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"ifExist","hash":"e2fe30fd8a4a4474eaabe7bbfb42b23b"}
res=requests.post(url=url,data=req)
print(res.text)

for i in range(4483,4489):
    req={"method":"delete","id":i,"password":"229028"}
    res=requests.post(url=url,data=req)
    print(res.text)