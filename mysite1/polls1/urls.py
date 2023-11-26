from django.urls import path
from .views import osoba_list, osoba_detail, stanowisko_view, osoba_update,OsobaDelete,view_person_view


urlpatterns = [
    path('osoby/', osoba_list, name='osoba-list'),
    path('osoby/<int:pk>/', osoba_detail, name='osoba-detail'),
    path('osoby/<int:pk>/update/', osoba_update, name='osoba-update'),
    path('osoby/delete/<int:pk>/', OsobaDelete.as_view(), name='osoba-delete'),
    path('stanowiska/', stanowisko_view, name='stanowiska-list'),
    path('stanowiska/<int:pk>/', stanowisko_view, name='stanowisko-detail'),

    path('osoby/<int:pk>/view/', view_person_view, name='osoba-view'),

]
