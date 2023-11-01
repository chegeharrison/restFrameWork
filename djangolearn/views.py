from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from djangolearn.models import Location
from djangolearn.serializer import LocationSerializer


# Create your views here.
@api_view(['GET','POST'])
def mylocation(request):
    if request.method == 'GET':
        snippets = Location.objects.all()
        serializer = LocationSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

