from pics.models import pictures
from django.db import DatabaseError
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
import hashlib
import random as rd
from . import logger

admin_password_hash = ["50fbccb1d90ad0073f52ec277efaedad",]

def get_random_url():
    item = pictures.objects.all()[rd.randint(0,pictures.objects.count()-1)]
    name = item.name
    id_ = item.id
    source = item.source
    return {'id':id_, 'name':name, 'source':source}
    
def get_random_item():
    item = pictures.objects.all()[rd.randint(0,pictures.objects.count()-1)]
    return item

def get_item_by_name(path:str):
    try:
        pic = pictures.objects.get(name=path)
        return pic
    except pictures.DoesNotExist:
        return -1
    except pictures.MultipleObjectsReturned as e:
        logger.errorLog(e,"Multiple Objects Returned With Same Name: "+path)
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
        pic = pictures.objects.get(md5=h)
        return pic
    except pictures.DoesNotExist:
        return -1
    except pictures.MultipleObjectsReturned as e:
        logger.errorLog(e,"Multiple Objects Returned With Same Hash: "+h)
        return pictures.objects.all(md5=h)[0]
    
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
            logger.errorLog(e)
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
            logger.errorLog(e)
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
            logger.errorLog(e)
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
    if authors != None and authors != "":
        authors = authors.split("#")
        for author in authors:
            qset = qset.filter(author__contains=author)
    if characters != None and characters != "":
        characters = characters.split("#")
        for character in characters:
            qset = qset.filter(character__contains=character)
    if tags != None and tags != "":
        tags = tags.split("#")
        for tag in tags:
            qset = qset.filter(Q(tags__contains=tag)|Q(character__contains=tag)|Q(author__contains=tag))
    order = dic.get("order")
    if order == "likes":
        qset = qset.order_by("likes","id")
    elif order == "likes_r":
        qset = qset.order_by("-likes","id")
    elif order == "random":
        qset = qset.order_by("?")
    elif order == "id_r":
        qset = qset.order_by("-id")
    else:
        qset = qset.order_by("id")
    pages = Paginator(qset.values_list("id", flat=True),20)
    try:
        page = dic.get("page")
        if  page == None:
            page = 1
        return list(pages.page(page))
    except InvalidPage:
        return -1
    except Exception as e:
        logger.errorLog(e)
        return -2

def random_item_by_tag(dic:dict):
    authors = dic.get("author")
    characters = dic.get("character")
    tags = dic.get("tags")
    qset = pictures.objects.all()
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
    if qset.count() == 0:
        return -1
    return qset[rd.randint(0,qset.count()-1)]

def upload(dic:dict):
    name_ = dic.get("name")
    if name_ == None:
        return -1
    md5_ = dic.get("md5")
    if md5_ == None:
        md5_ = "default"
    else:
        if if_hash_exist(md5_) == 1:
            try:
                pic = pictures.objects.get(md5=md5_)
            except pictures.MultipleObjectsReturned:
                logger.errorLog(e,"Multiple Objects Returned With Same Hash: "+md5_)
                pic = pictures.objects.all(md5=md5_)[0]
            return pic
    if get_item_by_name("name_") != -1:
        return get_item_by_name(name_)
    author_ = dic.get("author")
    if author_ == None:
        author_ == ""
    character_ = dic.get("character")
    if character_ == None:
        character_ == ""
    tags_ = dic.get("tags")
    if tags_ == None:
        tags_ == ""
    try:
        pictures.objects.create(name=name_,md5=md5_,author=author_,character=character_,tags=tags_,source=0,likes=0)
    except Exception as e:
        logger.errorLog(e)
        return -2
    return get_item_by_name(name_)

def delete(dic:dict):
    pw = dic.get("password")
    if pw == None:
        return -2
    if hashlib.md5(pw.encode('utf-8')).hexdigest() not in admin_password_hash:
        return -2
    id_ = dic.get("id")
    try:
        pic = pictures.objects.get(id=id_)
    except pictures.DoesNotExist:
        return -1
    pic.delete()
    return 1

def merge(dic:dict):
    pw = dic.get("password")
    if pw == None:
        return -2
    if hashlib.md5(pw.encode('utf-8')).hexdigest() not in admin_password_hash:
        return -2
    id_main = dic.get("id_main")
    ids = dic.getlist("ids")
    try:
        pic_main = pictures.objects.get(id=id_main)
    except pictures.DoesNotExist:
        return -1
    if pic_main.author != None:
        authors_main = set(pic_main.author.split('#'))
    else:
        authors_main = set()
    if pic_main.character != None:
        characters_main = set(pic_main.character.split('#'))
    else:
        characters_main = set()
    if pic_main.tags != None:
        tags_main = set(pic_main.tags.split('#'))
    else:
        tags_main = set()
    for id_ in ids:
        try:
            pic = pictures.objects.get(id=id_)
        except pictures.DoesNotExist:
            return -1
        if pic.author != None:
            authors = pic.author.split('#')
            for author in authors:
                authors_main.add(author)
        if pic.character != None:
            characters = pic.character.split('#')
            for character in characters:
                characters_main.add(character)
        if pic.tags != None:
            tags = pic.tags.split('#')
            for tag in tags:
                tags_main.add(tag)
        pic_main.likes += pic.likes
    authors_final = ""
    characters_final = ""
    tags_final = ""
    for author in authors_main:
        authors_final += "#"
        authors_final += author
    for character in characters_main:
        characters_final += "#"
        characters_final += character
    for tag in tags_main:
        tags_final += "#"
        tags_final += tag
    try:
        pic_main.author = authors_final
        pic_main.character = characters_final
        pic_main.tags = tags_final
        pic_main.save()
    except DatabaseError:
        return -3
    except Exception as e:
        logger.errorLog(e)
        return -4    
    for id_ in ids:
        pic = pictures.objects.get(id=id_)
        pic.delete()
    return pic_main