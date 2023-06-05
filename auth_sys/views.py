from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token

from .models import Profile, Users
from .serializers import UsersSerializer, ProfileSerializer



class APIOverview(APIView):
    def get(self,request, format=None):
        profiles = Profile.objects.all().order_by('-fullname')
        serializer = ProfileSerializer(profiles, many=True)

        return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def loadSignup( request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = Users.objects.create(email=data['email'])
            user.save()
            profile = Profile.objects.create(user=user, fullname=data['fullname'])
            profile.save()

            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {"error":"email already exists"},
                status=400
            )


@api_view(['POST'])
@csrf_exempt
def loadLogin(request):
    if request.method == 'POST':
       data = JSONParser().parse(request)
       user = authenticate(request, username=data['email'].lower())

       if user is None:
           return JsonResponse({"error": "unable to login, check email"}, status=400)
       else:
           try:
               token = Token.objects.get(user=user)
           except:
               token = Token.objects.create(user=user)
           return JsonResponse({"token":str(token)}, status=201)
               


# class APIOverview(generics.ListAPIView):
#     def get(self,request, format=None):
#         profiles = Profile.objects.all().order_by('-fullname')
#         serializer = ProfileSerializer(profiles, many=True)

#         return Response(serializer.data)
    

# class APICreate(generics.CreateAPIView):
#     @csrf_exempt
#     def post(self, request, format=None):
#         if self.request.method == 'POST':
#             try:
#                 data = JSONParser().parse(request)
#                 user = Users.objects.create(email=data['email'])
#                 user.save()
#                 profile = Profile.objects.create(user=user, fullname=data['fullname'])
#                 profile.save()

#                 token = Token.objects.create(user=user)
#                 return JsonResponse({'token':str(token)}, status=201)
#             except IntegrityError:
#                 return JsonResponse(
#                     {"error":"email already exists"},
#                     status=400
#                 )