from datetime import datetime
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.generic.base import View
from rest_framework import decorators
from fatema.models import clientmst
from fatema.models import Project
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
from django.http import HttpResponse

from fatema.serializers import ClientSerializer
from fatema.serializers import projectSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@api_view(['GET'])
def clientList(request):
    result = clientmst.objects.all()
    serializer = ClientSerializer(result, many=True)
    return Response({'message': 'success', 'status': 'True', 'data': serializer.data})

@api_view(['POST'])
def clientAdd(request):
    clientname = request.data.get('clientname')
    created_by = request.user.id
    
    client = clientmst(clientname=clientname,created_by_id=created_by)
    serializer = ClientSerializer(instance=client,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Add Successfully', 'status': 'True', 'data': serializer.data})
    else:
        return Response({'message': 'Error', 'status': 'False', 'data': []})


@api_view(['GET'])
def projectlist(request):
    result1 =Project.objects.all()
    serializer = projectSerializer(result1, many=True)
    return Response({'message': 'success', 'status': 'True', 'data': serializer.data}) 


@method_decorator(csrf_exempt,name='dispatch')
class clientUpdate(View):


     def patch(self,request,client_id):
         data=json.loads(request.body.decode("utf-8"))
         client=clientmst.objects.get(id=client_id)
         client.client_name=data['client_name']
         client.save()

         data={
             'message':f'Client {client_id} has been updated'
         }
         return JsonResponse(data)


   

@method_decorator(csrf_exempt,name='dispatch')
class clientDelete(View):


     def patch(self,request,client_id):
         data=json.loads(request.body.decode("utf-8"))
         client=clientmst.objects.get(id=client_id)
         client.client_name=data['client_name']
         client.save()

         data={
             'message':f'Client {client_id} has been updated'
         }
         return JsonResponse(data)

         ...
     def delete(self,request,client_id):
        client=clientmst.objects.get(id=client_id)
        client.delete() 
        data={
             'message':f'Client {client_id} has been deleted'
         }
        return JsonResponse(data) 

class HttpResponseNoContent(HttpResponse):
     status_code=204
def my_view(request):
    return HttpResponseNoContent()      
           





