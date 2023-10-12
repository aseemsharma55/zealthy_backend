from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import user_query
import json
from .serializer import userSerializer
# Create your views here.


class UserQuery(APIView):
    def post(self,request,format='json'):
        try:
            request_body = json.loads((request.body))
            print(request_body)
            name=request_body["name"]
            email=request_body["email"]
            desc=request_body["description"]
            user_query_obj = user_query(name=name, email=email, desc=desc, status="New")
            user_query_obj.save()
            return JsonResponse({"result":"Success!"})
        except Exception as e:
            return JsonResponse({"result":"Failure","Error":str(e)})
            

    
class GetUserQuery(APIView):
    def get(self,request,format='json'):
        try:
            data = user_query.objects.all()
            user_data=userSerializer(data,many=True).data
            print(user_data)
            
            return JsonResponse({"result":"Success!",'data':user_data})
        except Exception as e:
            return JsonResponse({"result":"Failure","Error":str(e)})
            

class AdminUpdate(APIView):
    def post(self,request,format='json'):
        try:
            request_body = json.loads((request.body))
            print(request_body)
            email=request_body["email"]
            status = request_body["status"]
            user_obj = user_query.objects.get(email=email)
            user_obj.status = status
            user_obj.save()
            return JsonResponse({"result":"success"})
        except Exception as e:
            return JsonResponse({"result":"Failure","Error":str(e)})


class UserQueryStatus(APIView):
    def post(self,request,format='json'):
        try:
            request_body = json.loads((request.body))
            print(request_body)
            email=request_body["Email"]
            user_obj = user_query.objects.get(email=email)
            status = user_obj.status
            return JsonResponse({"result":"success","status":status})
        except Exception as e:
            return JsonResponse({"result":"Failure","Error":str(e)})
        
