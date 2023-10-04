from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from . import db
from . import logger
from qiniu import Auth

base_path=["http://s1by40tsq.hn-bkt.clouddn.com/",
           "",]

server_url="http://120.26.195.153:1096/api/"

def std_item_res(item):
    return JsonResponse({"id":item.id, 'url':base_path[item.source] + item.name, 'author':item.author, 'character':item.character, 'tags':item.tags, 'likes':item.likes})

def api(request):

    if request.POST:
        req = request.POST
    else:
        req = json.loads(request.body)

    method = req.get("method")

    if method == "getRandomUrl":
        dbres = db.get_random_url()
        return JsonResponse({"id":dbres["id"], 'url':base_path[dbres["source"]] + dbres["name"],'Access-Contro1-Allow-origin':"*"})
    
    elif method == "getRandomItem":
        dbres = db.get_random_item()
        return std_item_res(dbres)
    
    elif method == "getItemById":
        dbres = db.get_item_by_id(req.get("id"))
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        return std_item_res(dbres)
    
    elif method == "getItemByName":
        dbres = db.get_item_by_name(req.get("name"))
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        return std_item_res(dbres)
    
    elif method == "searchByTag":
        dbres = db.search_ids_by_tag(req)
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        elif dbres == -2:
            return JsonResponse({"message":"error"})
        return JsonResponse({"ids":dbres})
    
    elif method == "randomItemByTag":
        dbres = db.random_item_by_tag(req)
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        elif dbres == -2:
            return JsonResponse({"message":"error"})
        return std_item_res(dbres)
    
    elif method == "ifExist":
        dbres = db.if_hash_exist(req.get("hash"))
        if dbres == -1:
            return JsonResponse({"exist":"false"})
        else:
            try:
                return std_item_res(dbres)
            except:
                return JsonResponse({"message":"error"})
    
    elif method == "addTag":
        dbres = db.add_tag(req)
        if dbres == -1:
            return JsonResponse({"message":"Too Long"})
        elif dbres == -2:
            return JsonResponse({"message":"Invalid Text"})
        elif dbres == -3:
            return JsonResponse({"message":"Not Found"})
        elif dbres == -4:
            return JsonResponse({"message":"error"})
        else:
            return std_item_res(dbres)
        
    elif method == "editTag":
        dbres = db.edit_tag(req)
        if dbres == -1:
            return JsonResponse({"message":"Too Long"})
        elif dbres == -2:
            return JsonResponse({"message":"Invalid Text"})
        elif dbres == -3:
            return JsonResponse({"message":"Not Found"})
        elif dbres == -4:
            return JsonResponse({"message":"error"})
        else:
            return std_item_res(dbres)
        
    elif method == "report":
        reason = req.get("reason")
        id_ = req.get("id")
        detail = req.get("detail")
        dbres = db.get_item_by_id(id_)
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        if reason == None:
            return JsonResponse({"message":"Invalid Text"})
        url = base_path[dbres.source] + dbres.name
        if detail == None:
            logger.reportLog(id_,url,reason)
        else:
            logger.reportLog(id_,url,reason,detail)
        return JsonResponse({"message":":)"})

    elif method == "similar":
        id_ = req.get("id_main")
        ids = req.get("ids")
        if id_ == None:
            return JsonResponse({"message":"Invalid Id"})
        if ids == None:
            return JsonResponse({"message":"Invalid Id"})
        dbres = db.get_item_by_id(id_)
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        url = base_path[dbres.source] + dbres.name
        urls = []
        for i in ids:
            if dbres == -1:
                return JsonResponse({"message":"Not Found"})
            urls.append(base_path[dbres.source] + dbres.name)
        logger.similarLog(id_,url,ids,urls)
        return JsonResponse({"message":":)"})
        
    elif method == "like":
        dbres = db.like(req.get("id"))
        if dbres == 1:
            return JsonResponse({"message":":)"})
        else:
            return JsonResponse({"message":"error"})
        
    elif method == "getUploadToken":
        keys = open("/root/qiniuKeys.txt","r")
        keys = keys.read().splitlines()
        q = Auth(keys[0],keys[1])
        bucket_name = 'touhou-emoticon'
        name = req.get("name")
        dbres = db.get_item_by_name(name)
        if dbres != -1:
            return std_item_res(dbres)
        policy = {
         #'callbackUrl':server_url,
         #'callbackBody':'filename=$(fname)',
        }
        logger.uploadStartLog(name)
        token = q.upload_token(bucket_name, name, 3600, policy)
        return JsonResponse({"key":token})
    
    elif method == "upload":
        dbres = db.upload(req)
        if dbres == -2:
            return JsonResponse({"message":"error"})
        logger.uploadLog(req["name"],req["md5"])
        return std_item_res(dbres)

    elif method == "delete":
        dbres = db.delete(req)
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        elif dbres == -2:
            return JsonResponse({"message":"Permission Denied"})
        elif dbres == -3:
            return JsonResponse({"message":"error"})
        else:
            return JsonResponse({"message":":)"})
        
    elif method == "merge":
        dbres = db.merge(req)
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        elif dbres == -2:
            return JsonResponse({"message":"Permission Denied"})
        elif dbres == -3:
            return JsonResponse({"message":"Too Long"})
        elif dbres == -4:
            return JsonResponse({"message":"error"})
        else:
            return std_item_res(dbres)

    else:
        return JsonResponse({"message":"连接成功"})

def random(request):
    context = {}
    dbres = db.get_random_url()
    context['url'] = base_path[dbres["source"]] + dbres["name"]
    return render(request, 'plainpic.html', context)

def randoms(request):
    return render(request, 'randomPics.html')

def search(request):
    return render(request, 'search.html')

def singlePic(request):
    context = {}
    pic = db.get_item_by_name(request.path[1:])
    if pic==-1:
        return HttpResponse("请求的对象不存在")
    context['url'] = base_path[pic.source] + pic.name
    return render(request, 'singlepic.html', context)
