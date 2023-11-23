import datetime
import json
from sre_parse import State
from turtle import title
from wsgiref import headers
from .models import Book
from BooksDilemma.models import BookCategory, BookDilemma, BookDimension, DilemmaPerBook
from .serializers import BookSerializer, BookUpdatedBySerializer, bookStateSerializer
from BooksDilemma.serializers import BookCategorySerializer, BookDimensionSerializer, BookDilemmaSerializer, DilemmaPerBookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import hashlib
from django.db.models import Prefetch
import sys
sys.path.append('funread_backend')
import verifyJwt
from django.db import OperationalError



@api_view(['POST'])
def new_book(request):

    #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
     data = {
        'title': request.data.get('title'),
        'category': request.data.get('category'),
        'portrait': request.data.get('portrait'),
        'createdby': request.data.get('createdby'),
        'createdat': datetime.datetime.now(),
        'updatedby': request.data.get('updatedby'),
        'lastupdateat': datetime.datetime.now(),
        'state' : request.data.get('state' ),
        'sharedbook' : request.data.get('sharedbook'),
        'lastupdateby': request.data.get('lastupdateby'),
        'description': request.data.get('description')
     }
     serializer = BookSerializer(data=data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def bookSearch(request, title):

    #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    
     print(title)
     book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)
   

@api_view(['PUT'])
def bookChange(request):

    #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    
     dataRequest = {
            'title': request.data.get('title'),
     }
     titleSe = dataRequest.get('title')
     book = Book.objects.get(title=titleSe)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    try:
     data = {
        'title': request.data.get('new_title'),
        'portrait': request.data.get('portrait'),
        'category': request.data.get('category'),
        'createdby': request.data.get('createdby'),
        'updatedby': request.data.get('updatedby'),
        'lastupdateat': datetime.datetime.now(), 
        'state': request.data.get('state'),
        'description': request.data.get('description')
     }
     serializer = BookSerializer(book, data=data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ api_view(['GET'])
def listed(request):

           #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

     # Utilizamos select_related para obtener la información relacionada en una sola consulta
     books = Book.objects.all()
     book_serializer = BookSerializer(books, many=True)
    except OperationalError:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    response_data = []

    for book in book_serializer.data:
        dilemmasperbook = DilemmaPerBook.objects.filter(bookid=book['bookid'])
        dilemmasperbook_serializer = DilemmaPerBookSerializer(dilemmasperbook, many=True)

        dilemmas_ids = [dilemmasperbook['bookdilemmaid'] for dilemmasperbook in dilemmasperbook_serializer.data]
        dilemmas = BookDilemma.objects.filter(pk__in=dilemmas_ids)
        dilemmas_serializer = BookDilemmaSerializer(dilemmas, many=True)

        dimension_ids = [dilemma['bookdimensionid'] for dilemma in dilemmas_serializer.data]
        dimensions = BookDimension.objects.filter(pk__in=dimension_ids)
        dimensions_serializer = BookDimensionSerializer(dimensions, many=True)

        category_ids = [dimension['bookcategoryid'] for dimension in dimensions_serializer.data]
        categories = BookCategory.objects.filter(pk__in=category_ids)
        categories_serializer = BookCategorySerializer(categories, many=True)

        book_data = {
            'book_details': book,
            'book_context': {
                'dilemmas': dilemmas_serializer.data,
                'dimensions': dimensions_serializer.data,
                'categories': categories_serializer.data
            }
        }

        response_data.append(book_data)

    return Response(response_data, status=status.HTTP_200_OK)







    #token verification
    # try:
    #  authorization_header = request.headers.get('Authorization')
    #  verify = verifyJwt.JWTValidator(authorization_header)
    #  es_valido = verify.validar_token()
    #  if es_valido==False:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    #  book = Book.objects.all()
    #  serializer = BookSerializer(book, many=True)
    #  return Response(serializer.data)
    # except OperationalError:
    #      return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ api_view(['GET'])
def listed_PublishedBooks(request):

    #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
     book = Book.objects.filter(sharedbook=1)
     serializer = BookSerializer(book, many=True)
     return Response(serializer.data)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@ api_view(['GET'])
def listed_NotPublishedBooks(request):

    #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
     book = Book.objects.filter(sharedbook=2)
     serializer = BookSerializer(book, many=True)
     return Response(serializer.data)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@ api_view(['GET'])
def listed_PrivateBooks(request):

    #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
     book = Book.objects.filter(sharedbook=0)
     serializer = BookSerializer(book, many=True)
     return Response(serializer.data)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def modifyStateToPrivate(request):

    #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
     dataRequest = {
            'title': request.data.get('title'),
     }
     titleSe = dataRequest.get('title')
     book = Book.objects.get(title=titleSe)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
    try: 
     data = {
        'sharedbook': 0,
     }
     serializer = bookStateSerializer(book, data=data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def modifyStateToPublish(request):

    #token verification
    try:
     authorization_header = request.headers.get('Authorization')
     verify = verifyJwt.JWTValidator(authorization_header)
     es_valido = verify.validar_token()
     if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    
     dataRequest = {
            'title': request.data.get('title'),
     }
     titleSe = dataRequest.get('title')
     book = Book.objects.get(title=titleSe)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
    try: 
     data = {
        'sharedbook': 1,
     }
     serializer = bookStateSerializer(book, data=data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except OperationalError:
         return Response({"error": "Error en la base de datos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
