import requests

url="http://127.0.0.1:1096/api/"
req={"method":"getRandomUrl"}
res=requests.post(url=url,data=req)
print(res.text)

'''req={"method":"getRandomItem"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"getItemById", "id":"114"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"getItemByName", "name":"a65fb97d520fcebe0495517e10cf6b88780831d6.jpg"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"ifExist","hash":"399c85ab47828e8997fb53a7a1416905d45ac8ce"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"like","id":"1145"}
res=requests.post(url=url,data=req)
print(res.text)

req={"method":"getItemById","id":"114"}
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
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"getItemByName","name":"01f05546bb9e188a443b572431d1c6d0be67b7f5.jpg"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"randomItemByTag","character":"⑨","tags":"#笨蛋#baka"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"searchByTag","character":"⑨","tags":"#笨蛋#baka","page":"1","order":"id_r"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"report","id":"1145","reason":"太可爱了"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))'''

'''req={"method":"upload","name":"testitem1","author":"#test1#test11","tags":"#test1#test11","character":"#test1#test11"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"upload","name":"testitem2","author":"#test2#test22","tags":"#test2#test22","character":"#test2#test22"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"upload","name":"testitem3","author":"#test3#test33","tags":"#test3#test33","character":"#test3#test33"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"upload","name":"testitem4","author":"test4","tags":"test4","character":"test4"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"upload","name":"testitem4","author":"test4","tags":"test4","character":"test4"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))'''

'''req={"method":"getItemById","id":"4453"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"delete","id":"4453","password":"229028"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))'''

'''req={"method":"merge","id_main":"4450","ids":[4451,4452],"password":"229028"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))'''

'''req={"method":"getItemById","id":"4450"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"getItemById","id":"4451"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"getItemById","id":"4452"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"delete","id":"4450","password":"229028"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))'''

req={"method":"searchByTag","tags":"#笨蛋"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

req={"method":"getItemById","id":"1145"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))



req={"method":"editTag","id":"1145","character":"#火焰猫燐#阿燐"}
res=requests.post(url=url,data=req)
print(res.text.encode('utf-8').decode('unicode_escape'))

