#from django.http import HttpResponse
#from django.shortcuts import render
# Create your views here.

#def myIndex(request):
 #   my_name = request.GET.get('name' , "CGU")
  #  #my_name = request.POST.get('name' , "CGU")
   # return HttpResponse("Hello " + my_name)

#from _typeshed import SupportsLessThanT
from typing import AsyncContextManager
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
from .models import personal_account
import logging
import json
logger=logging.getLogger('django')


@api_view(['GET'])
def add_post(request):
    account = request.GET.get('account','')
    password = request.GET.get('password', '')
    name = request.GET.get('id', '')
  
    personal_data = personal_account()
    personal_data.account = account 
    personal_data.password = password 
    personal_data.name = name
    
    #logger.debug("************ myhello api" + title)
    #if title:
    #    return Response({"data" : title +"insert!"}, status = status.HTTP_200_OK)
    #else:
    #    return Response(
    #        {"res":"parameter : name is None"},
    #        status = status.HTTP_400_BAD_REQUEST
    #    )
@api_view(['GET'])
def list_post(resquest):
    personal = personal_account.objects.all().values()
    return JsonResponse(list(personal),safe=False)
    #return Response({"data":
    #    json.dump(
    #    list(personal),
    #    sort_keys = True,
    #    indent = 1, 
    #    cls = DjangoJSONEncoder)},
    #    status = status .HTTP_200_OK
    #    )

'''class HelloApiView(APIView):
    def get(self, request):
        my_name = request.GET.get('name' , None)
        if my_name:
            retValue = {    }
            retValue['data'] = "Hello" + my_name
            return Response(retValue, status=status.HTTP_200_OK)
        else:
            return Response (
                {"res": "parameter: name is None"},
                status=status.HTTP_400_BAD_REQUEST
            )'''




