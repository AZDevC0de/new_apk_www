from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def osoba_list(request):
    if request.method == 'GET':
        nazwa = request.query_params.get('nazwa', None)
        if nazwa is not None:
            osoby = Osoba.objects.filter(nazwa__icontains=nazwa)
        else:
            osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

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


@api_view(['GET', 'PUT', 'DELETE'])
def osoba_detail(request, pk):
    """
    Pobiera, aktualizuje lub usuwa konkretny obiekt Osoba.
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)