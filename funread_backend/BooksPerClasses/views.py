from django.shortcuts import render
import datetime
import json
from sre_parse import State
from turtle import title
from wsgiref import headers
from .models import BooksPerClasses
from .serializers import BooksPerClassesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import hashlib

# Create your views here.

#Metodo para mostrar todos los elementos de la lista TagsPerPage
@ api_view(['GET'])
def listed(request):
    booksPerClasses = BooksPerClasses.objects.all()
    serializer = BooksPerClassesSerializer (booksPerClasses, many=True)
    return Response(serializer.data)

#Metodo para buscar una variable por nombre
@api_view(['GET'])
def search(request):
    try:
        booksPerClasses  = BooksPerClasses.objects.get(booksPerClassesId=request.data.get('booksPerClassesId'))
        print(booksPerClasses)
    except BooksPerClasses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BooksPerClassesSerializer(booksPerClasses)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Metodo para agregar un elemento a la lista SharedBooks
@api_view(['POST'])
def add_new(request):
    print(request.data)
    data = {
        'booksId': request.data.get('booksId'),
        'classesId': request.data.get('classesId'),
    }
    serializer = BooksPerClassesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#Elimina un elemento de la lista SharedBooks
@api_view(['DELETE'])
def delete(request):
    booksPerClasses = BooksPerClasses.objects.get(booksPerClassesId=request.data.get('booksPerClassesId'))
    booksPerClasses.delete()
    return Response({"msj":"Succesfully deleted"}, status=status.HTTP_200_OK)


#Metedo que cambia la variable de la lista SharedBooks
@api_view(['PUT'])
def update(request):
    booksPerClasses  = BooksPerClasses .objects.get(booksPerClassesId=request.data.get('booksPerClassesId'))
    serializer = BooksPerClassesSerializer(booksPerClasses, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

