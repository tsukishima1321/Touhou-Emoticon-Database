import requests

url="http://127.0.0.1:1096/api/"
'''req={"method":"getRandomUrl"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"getRandomItem"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"getItemById", "id":"114"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"getItemByName", "name":"a65fb97d520fcebe0495517e10cf6b88780831d6.jpg"}
res=requests.post(url=url,data=req)
print(res.text)'''

req={"method":"ifExist","hash":"399c85ab47828e8997fb53a7a1416905d45ac8ce"}
res=requests.post(url=url,data=req)
print(res.text)