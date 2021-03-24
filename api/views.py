from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, views
from .models import *
from bs4 import BeautifulSoup
import requests

from .stores.ekonga import *
from .stores.jumia import *



from rest_framework.decorators import api_view
@api_view(['GET'])
def action(request):
    try :
        query = request.GET.__getitem__('query')
        url = "https://www.konga.com/search?search="
        url = url+query
        token, agent = cfscrape.get_tokens(url, 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 RuxitSynthetic/1.0 v6870249674 t38550 ath9b965f92 altpub cvcv=2, _optional_')
        jumia_title, jumia_img,jumia_link, jumia_price = jumia(query)
        ekonga_title, ekonga_img,ekonga_link,ekonga_price = ekonga(query)
        context ={'jumia': {
             'img' :jumia_img,
            'title': jumia_title,
            'price': jumia_price,
            "link" : jumia_link},
            
            "ekonga":{
            "img":ekonga_img,
            "title" :ekonga_title,
            "price": ekonga_price,
            "link":ekonga_link,
            
            }
        }
        return_object = {
            "Error": 0,
            "Message": "Success",
            "data": context
        }
        pass

        return Response(return_object)
        
    
    except Exception as e :
        print(e)
        return HttpResponse(e)




def index(request):

    context = {}
    return render(request,'index.html')

