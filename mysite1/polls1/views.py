from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from django.db.models import Q

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_list(request):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(wlasciciel=request.user)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def osoba_detail(request, pk):
    """
    Pobiera konkretny obiekt Osoba.
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OsobaSerializer(osoba)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
# def osoba_update_delete(request, pk):
#     """
#     Aktualizuje lub usuwa konkretny obiekt Osoba.
#     """
#     try:
#         osoba = Osoba.objects.get(pk=pk)
#     except Osoba.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         serializer = OsobaSerializer(osoba, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         osoba.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['PUT'])
def osoba_update(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OsobaSerializer(osoba, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    osoba.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def stanowisko_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            stanowisko = Stanowisko.objects.filter(pk=pk)
        else:
            stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StanowiskoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' and pk:
        stanowisko = Stanowisko.objects.get(pk=pk)
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


