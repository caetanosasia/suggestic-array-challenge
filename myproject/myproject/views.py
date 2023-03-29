from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from .serializers import ArraySerializer
from .models import Array

@api_view(['POST'])
def normalize_array(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArraySerializer(data=data)
        if serializer.is_valid():
            #serializer.save()
            print(Array.destructuring(data.get('input')))
            print('-----------------------------------')
            print(data.get('input'))
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Only POST requests are allowed")