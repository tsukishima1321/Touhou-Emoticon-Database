from Pics.models import pictures
from django.db import DatabaseError
from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
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
    author = dic.get("author")
    character = dic.get("character")
    tag = dic.get("tags")
    invalidc = "!@$%^&*()+-*/<>,.[]\\\{\}\'\""
    if author != None:
        #check valid
        for c in invalidc:
            if c in author:
                return -2
        #split text into tags
        authors = author.split('#')
        #for tag in tags check if exist
        authors_n = []
        if pic.author == None:
            pic.author = ""
        for author_tag in authors:
            if author_tag not in pic.author:
                authors_n.append(author_tag)
        try:
        #add to database
            for author_tag in authors_n:
                pic.author += ("#" + author_tag)
        except DatabaseError:
        #catch too long error
            return -1
        except Exception as e:
            print(repr(e))
            f = open("errorlog.txt","a")
            f.write(repr(e)+"\n")
            f.close()
    if character != None:
        #same
        for c in invalidc:
            if c in character:
                return -2
        characters = character.split('#')
        characters_n = []
        if pic.character == None:
            pic.character = ""
        for character_tag in characters:
                if character_tag not in pic.character:
                    characters_n.append(character_tag)
        try:
            for character_tag in characters_n:
                pic.character += ("#" + character_tag)
        except DatabaseError:
            return -1
        except Exception as e:
            print(repr(e))
            f = open("errorlog.txt","a")
            f.write(repr(e)+"\n")
            f.close()
            return -4
    if tag != None:
        #same
        for c in invalidc:
            if c in tag:
                return -2
        tags = tag.split('#')
        if pic.tags == None:
            pic.tags = ""
        tags_n = []
        for tag_tag in tags:
            if tag_tag not in pic.tags:
                tags_n.append(tag_tag)
        try:
            for tag_tag in tags_n:
                pic.tags += ("#" + tag_tag)
        except DatabaseError:
            return -1
        except Exception as e:
            print(repr(e))
            f = open("errorlog.txt","a")
            f.write(repr(e)+"\n")
            f.close()
    try:
        pic.save()
    except DatabaseError:
        return -1
    return pic


def edit_tag(dic:dict):
    try:
        pic = pictures.objects.get(id=dic.get("id"))
    except pictures.DoesNotExist:
        return -3
    author = dic.get("author")
    character = dic.get("character")
    tag = dic.get("tags")
    invalidc = "!@$%^&*()+-*/<>,.[]\\\{\}\'\""
    if author != None:
        #check valid
        for c in invalidc:
            if c in author:
                return -2
        #update database
        pic.author = author
    if character != None:
        #same
        for c in invalidc:
            if c in character:
                return -2
        pic.character = character
    if tag != None:
        #same
        for c in invalidc:
            if c in tag:
                return -2
        pic.tags = tag
    try:
        pic.save()
    except DatabaseError:
        return -1
    return pic

def like(id_:int):
    try:
        pic = pictures.objects.get(id=id_)
        pic.likes += 1
        pic.save()
        return 1
    except pictures.DoesNotExist:
        return -1
    
def search_ids_by_tag(dic:dict):
    authors = dic.get("author")
    characters = dic.get("character")
    tags = dic.get("tags")
    qset = pictures.objects.values("id")
    if authors != None:
        authors = authors.split("#")
        for author in authors:
            qset = qset.filter(author__contains=author)
    if characters != None:
        characters = characters.split("#")
        for character in characters:
            qset = qset.filter(character__contains=character)
    if tags != None:
        tags = tags.split("#")
        for tag in tags:
            qset = qset.filter(tags__contains=tag)
    order = dic.get("order")
    if order == "likes":
        qset = qset.order_by("likes")
    elif order == "random":
        qset = qset.order_by("?")
    else:
        qset = qset.order_by("id")
    pages = Paginator(qset,20)
    try:
        page = dic.get("page")
        if  page == None:
            page = 1
        return list(pages.page(page).object_list)
    except InvalidPage:
        return -1
    except:
        return -2



def random_item_by_tag(dic:dict):
    pass