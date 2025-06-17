from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .models import *

class userSignup(APIView):
    def post(self,request):
        SerializerData =userDetailsSerializer(data=request.data)
        if SerializerData.is_valid():
            userdetails.objects.create(**SerializerData.data)
            message ={"message": "User Signup Successfully"}
            return JsonResponse(message)
        return JsonResponse(SerializerData.errors)
    

class userMembership(APIView):
     def get(self,request,email):
            result =list(membershipdetails.objects.filter(email=email).values())
            message ={"userMembershipDetails":result}
            return JsonResponse(message)
    
        
