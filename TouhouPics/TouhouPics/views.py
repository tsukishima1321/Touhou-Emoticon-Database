from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import db

base_path="http://i0.hdslb.com/bfs/article/"

def std_item_res(item):
    return JsonResponse({"id":item.id, 'url':base_path + item.name, 'author':item.author, 'character':item.character, 'tags':item.tags, 'likes':item.likes})

def api(request):

    method = request.POST.get("method")

    if method == "getRandomUrl":
        dbres = db.get_random_url()
        return JsonResponse({"id":dbres["id"], 'url':base_path + dbres["name"]})
    
    elif method == "getRandomItem":
        dbres = db.get_random_item()
        return std_item_res(dbres)
    
    elif method == "getItemById":
        dbres = db.get_item_by_id(request.POST.get("id"))
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        return std_item_res(dbres)
    
    elif method == "getItemByName":
        dbres = db.get_item_by_name(request.POST.get("name"))
        if dbres == -1:
            return JsonResponse({"message":"Not Found"})
        return std_item_res(dbres)
    
    elif method == "ifExist":
        dbres = db.if_hash_exist(request.POST.get("hash"))
        if dbres == 1:
            return JsonResponse({"exist":"true"})
        elif dbres == -1:
            return JsonResponse({"exist":"false"})
        return JsonResponse({"message":"error"})
    
    elif method == "addTag":
        dbres = db.add_tag(request.POST)
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
        dbres = db.edit_tag(request.POST)
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
        
    elif method == "like":
        dbres = db.like(request.POST.get("id"))
        if dbres == 1:
            return JsonResponse({"message":":)"})
        else:
            return JsonResponse({"message":"error"})

    else:
        return JsonResponse({"message":"连接成功"})

def random(request):
    context = {}
    context['url'] = base_path + db.get_random()
    return render(request, 'plainpic.html', context)

def singlePic(request):
    context = {}
    pic = db.get_item_by_name(request.path[1:])
    if pic==-1:
        return HttpResponse("请求的对象不存在")
    context['url'] = base_path + pic.name
    return render(request, 'singlepic.html', context)
