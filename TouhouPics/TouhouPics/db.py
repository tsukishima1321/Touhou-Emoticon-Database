from Pics.models import pictures
import random as rd
import os

def get_random():
    url = pictures.objects.all()[rd.randint(0,pictures.objects.count()-1)].name
    return url

def get_single(path):
    try:
        pic = pictures.objects.get(name=path[1:])
        return pic
    except pictures.DoesNotExist as e:
        return -1
    except pictures.MultipleObjectsReturned as e:
        f = open("errorlog.txt","a")
        f.write("MultipleObjectsReturned: "+path+"\n")
        f.close()
        #delete from pics_pictures where id not in ( select dt.id from ( select min(id) as id from pics_pictures group by name ) dt)
        pic = pictures.objects.filter(name=path[1:])[0]
        return pic