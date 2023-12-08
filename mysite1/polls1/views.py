from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
# Create your views here.
# @login_required
#

# def osoba_view(request, pk):
#     if not request.user.has_perm('polls1.view_osoba'):
#         raise PermissionDenied()
#     try:
#         osoba = Osoba.objects.get(pk=pk)
#         return HttpResponse(f"Ta osoba nazywa się {osoba.imie} {osoba.nazwisko}")
#     except Osoba.DoesNotExist:
#         return HttpResponse("W bazie nie ma osoby o podanym ID.")
@api_view()
def view_person_view(request, pk):
    if request.user.has_perm('polls1.view_osoba'):
        try:
            person = Osoba.objects.get(pk=pk)

            return Response(
                {'message': f'Ten użytkownik nazywa się {person.imie}'}
            )

        except Osoba.DoesNotExist:
            return Response(
                {'message': f'W bazie nie ma użytkownika o id={pk}'},
                status=status.HTTP_404_NOT_FOUND
            )

    if request.user.has_perm('polls1.view_other_osoba'):
        try:
            person = Osoba.objects.get(pk=pk)

            if request.user.pk != person.wlasciciel.pk:
                return Response(
                    {'message': f'Ten użytkownik nazywa się {person.imie}'}
                )

        except Osoba.DoesNotExist:
            return Response(
                {'message': f'W bazie nie ma użytkownika o id={pk}'},
                status=status.HTTP_404_NOT_FOUND
            )

    raise PermissionDenied()
@api_view(['GET', 'POST'])
# @authentication_classes([BasicAuthentication])
@authentication_classes([TokenAuthentication])
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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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


# @api_view(['PUT', 'DELETE'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def osoba_update_delete(request, pk):
#     """
#
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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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
#do zadania lab7
class OsobaDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = (IsAuthenticated, DjangoModelPermissions,)
    def delete(self,request, pk):
        try:
            get_object_or_404(Osoba, pk=pk).delete()

        except Osoba.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return Osoba.objects.filter(pk=self.kwargs['pk'])

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


