from django.shortcuts import render
from django.http import HttpResponse
from . import db

base_path="http://i0.hdslb.com/bfs/article/"

def random(request):
    context = {}
    context['url'] = base_path + db.get_random()
    return render(request, 'plainpic.html', context)

def singlePic(request):
    context = {}
    pic = db.get_single(request.path)
    if pic==-1:
        return HttpResponse("请求的对象不存在")
    context['url'] = base_path + pic.name
    return render(request, 'singlepic.html', context)