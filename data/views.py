from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework .response import Response
from .models import Employement
from .serializers import EmployementSeralizer
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/data/',
    ]
    return Response(routes)



@api_view(['GET'])
def getEdata(request):
    employements = Employement.objects.all()
    serializer = EmployementSeralizer(employements,many=True)
    return Response(serializer.data)

