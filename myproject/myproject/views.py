from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
import json
from rest_framework.parsers import JSONParser 
from .serializers import ArraySerializer,ArrayToReturnSerializer
from .models import Array

"""
curl --location 'http://0.0.0.0:8000/normalize-array/' \
--header 'Content-Type: application/json' \
--data '{
    "input": [1, 2, [3, 4, [5, 6], 7], 8, 10]
}'
"""

@api_view(['POST'])
def normalize_array(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArraySerializer(data=data)
        if serializer.is_valid():
            answ = (Array.destructuring(data.get('input')))
            answ = json.loads('{ "output": '+str(answ)+' }')
            answ = ArrayToReturnSerializer(data=answ)
            if(answ.is_valid()):
                answ.save()
                return JsonResponse(answ.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse(answ.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Only POST requests are allowed")