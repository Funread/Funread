import datetime
import json
from sre_parse import State
from turtle import title
from wsgiref import headers
from .models import Book
from .serializers import BookSerializer, BookUpdatedBySerializer, bookStateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import hashlib
import sys
sys.path.append('funread_backend')
import verifyJwt

# Create your views here.
@api_view(['GET'])
def bookSearch(request, title):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        print(title)
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


#  Metodos de Category ------------------------------------------------------------------------------------
@api_view(['GET'])
def search_category(request, bookdilemmaid):
    return 'a'

@api_view(['GET'])
def list_category(request):
    return 'a'

@api_view(['POST'])
def new_category(request):
    return 'a'

@api_view(['PUT'])
def change_category(request):
    return 'a'

#  Metodos de Dimension ------------------------------------------------------------------------------------
@api_view(['GET'])
def search_dimesion(request, bookdimensionid):
    return 'a'

@api_view(['GET'])
def list_dimesion(request):
    return 'a'

@api_view(['POST'])
def new_dimesion(request):
    return 'a'

@api_view(['PUT'])
def change_dimesion(request):
    return 'a'

#  Metodos de Dilemma ------------------------------------------------------------------------------------
@api_view(['GET'])
def search_dilemma(request,bookdilemmaid):
    return 'a'

@api_view(['GET'])
def list_dilemma(request):
    return 'a'

@api_view(['POST'])
def new_dilemma(request):
    return 'a'

@api_view(['PUT'])
def change_dilemma(request):
    return 'a'

#  Metodos de DilemmaPerBook ------------------------------------------------------------------------------------
@api_view(['GET'])
def search_dilemmaperbook(request,dilemmaperbookid):
    return 'a'

@api_view(['GET'])
def list_dilemmaperbook(request):
    return 'a'

@api_view(['POST'])
def new_dilemmaperbook(request):
    return 'a'

@api_view(['PUT'])
def change_dilemmaperbook(request):
    return 'a'

#  Metodos extras ------------------------------------------------------------------------------------
@api_view(['GET'])
def get_dilemmas_per_book(request,getdilemmasperbook):
    return 'a'

@api_view(['GET'])
def get_category_per_book(request,getcategoryperbook):
    return 'a'
