from Pics.models import pictures
import random as rd
import os

def get_random_url():
    item = pictures.objects.all()[rd.randint(0,pictures.objects.count()-1)]
    name = item.name
    id_ = item.id
    return {'id':id_, 'name':name}
    
def get_random_item():
    item = pictures.objects.all()[rd.randint(0,pictures.objects.count()-1)]
    return item

def get_item_by_name(path:str):
    try:
        pic = pictures.objects.get(name=path)
        return pic
    except pictures.DoesNotExist:
        return -1
    except pictures.MultipleObjectsReturned:
        f = open("errorlog.txt","a")
        f.write("Multiple Objects Returned With Same Name: "+path+"\n")
        f.close()
        #delete from pics_pictures where id not in ( select dt.id from ( select min(id) as id from pics_pictures group by name ) dt)
        pic = pictures.objects.filter(name=path)[0]
        return pic
    
def get_item_by_id(id_:int):
    try:
        pic = pictures.objects.get(id=id_)
        return pic
    except pictures.DoesNotExist:
        return -1
    
def if_hash_exist(h:str):
    try:
        pic = pictures.objects.get(hash_sha=h)
        return 1
    except pictures.DoesNotExist:
        return -1
    except pictures.MultipleObjectsReturned:
        f = open("errorlog.txt","a")
        f.write("Multiple Objects Returned With Same Hash: "+h+"\n")
        f.close()
        return 1
    
def add_tag(dic:dict):
    try:
        pic = pictures.objects.get(id=dic.get("id"))
    except pictures.DoesNotExist:
        return -3
    if dic.get("author") != None:
        #check valid
        #split text into tags
        #for tag in tags check if exist
        #add to database
        #catch too long error
        pass
    if dic.get("character") != None:
        #same
        pass
    if dic.get("tags") != None:
        #same
        pass


def edit_tag(dic:dict):
    try:
        pic = pictures.objects.get(id=dic.get("id"))
    except pictures.DoesNotExist:
        return -3
    if dic.get("author") != None:
        #check valid
        #check if too long
        #update database
        pass
    if dic.get("character") != None:
        #same
        pass
    if dic.get("tags") != None:
        #same
        pass

def like(id_:int):
    try:
        pic = pictures.objects.get(id=id_)
        pic.likes += 1
        pic.save()
        return 1
    except pictures.DoesNotExist:
        return -1