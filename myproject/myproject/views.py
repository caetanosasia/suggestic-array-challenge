from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def normalize_array(request):
    if request.method == "POST":
        if(request.body == b''):
            return HttpResponse("No data provided")
        if not request.body.items:
            return HttpResponse("No items in body provided")
        data = request.body.items
        data = data.decode('utf-8')
        data = data.split(',')
        data = [int(i) for i in data]
        data.sort()
        data = [str(i) for i in data]
        data = ','.join(data)
        return Response(data)
    else:
        return HttpResponse("Only POST requests are allowed")