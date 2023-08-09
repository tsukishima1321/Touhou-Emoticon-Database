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

'''req={"method":"ifExist","hash":"399c85ab47828e8997fb53a7a1416905d45ac8ce"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"like","id":"1145"}
res=requests.post(url=url,data=req)
print(res.text)'''

'''req={"method":"getItemById","id":"114"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"addTag","id":"114","character":"#恋恋#古明地恋agesrethrytrtseeeeerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"editTag","id":"114","character":"#恋恋"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"addTag","id":"114","character":"#恋恋#古明地恋"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"getItemById","id":"114"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))'''

'''req={"method":"getItemByName","name":"01f05546bb9e188a443b572431d1c6d0be67b7f5.jpg"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))'''

req={"method":"randomItemByTag","character":"⑨","tags":"#笨蛋#baka"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"searchByTag","character":"⑨","tags":"#笨蛋#baka","page":"1","order":"id_r"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"report","id":"1145","reason":"太可爱了"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))