from django.shortcuts import render
from Pics.models import pictures
import random as rd

def random(request):
    context = {}
    url = (pictures.objects.all()[rd.randint(0,pictures.objects.count()-1)]).name
    context['url'] = "http://i0.hdslb.com/bfs/article/"+ url
    return render(request, 'singlepic.html', context)