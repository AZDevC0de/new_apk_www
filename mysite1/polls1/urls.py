from django.urls import path
from .views import osoba_list, osoba_detail, stanowisko_view

urlpatterns = [
    path('osoby/', osoba_list, name='osoba-list'),
    path('osoby/<int:pk>/', osoba_detail, name='osoba-detail'),
    path('stanowiska/', stanowisko_view, name='stanowiska-list'),
    path('stanowiska/<int:pk>/', stanowisko_view, name='stanowisko-detail'),
]