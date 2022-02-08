from django.shortcuts import render
import requests
from .models import Memes


def home(request):
    response=requests.get('https://api.imgflip.com/get_memes').json()
    #print(len(response['data']['memes']))
    for i in range(len(response['data']['memes'])):
        if len(list(Memes.objects.filter(id=int(response['data']['memes'][i]['id']))))==0:
            item=Memes.objects.create(id=int(response['data']['memes'][i]['id']),name=response['data']['memes'][i]['name'],url=response['data']['memes'][i]['url'],width=response['data']['memes'][i]['width'],height=response['data']['memes'][i]['height'],box_count=response['data']['memes'][i]['box_count'],image=response['data']['memes'][i]['url'][8:])
            item.save()
    memes=Memes.objects.all()
    return render(request,'main.html',{'response':response,'memes':memes})
