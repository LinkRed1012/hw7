#from django.http import HttpResponse
#from django.shortcuts import render
# Create your views here.

#def myIndex(request):
 #   my_name = request.GET.get('name' , "CGU")
  #  #my_name = request.POST.get('name' , "CGU")
   # return HttpResponse("Hello " + my_name)

#from _typeshed import SupportsLessThanT


from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
from .models import Personal
import logging
import json
logger=logging.getLogger('django')


@api_view(['GET'])
def add_post(request):
    name = request.GET.get('name' , '')
    account = request.GET.get('account' , '')
    password = request.GET.get('password' , '')
    personal_data = Personal()
    personal_data.name = name
    personal_data.account = account 
    personal_data.password = password 
    personal_data.save()

    logger.debug("************ myhello api" + name)
    if name:
        return Response({"name":name +"insert!"}, status = status.HTTP_200_OK)
    else:
        return Response(
            {"res":"parameter:name is None"},
            status=status.HTTP_400_BAD_REQUEST
        )
@api_view(['GET'])
def list_post(resquest):
    personal = Personal.objects.all().values()
    #return JsonResponse(list(personal),safe=False)

    return Response({"data":
                    json.dumps(
                      list(personal),
                      sort_keys= True,
                      indent=1,
                      cls= DjangoJSONEncoder)},
                    status = status.HTTP_200_OK)

   



