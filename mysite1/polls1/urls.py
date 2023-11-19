from django.urls import path,include
from .views import osoba_list, osoba_detail, stanowisko_view, osoba_update,osoba_delete
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('osoby/', osoba_list, name='osoba-list'),
    path('osoby/<int:pk>/', osoba_detail, name='osoba-detail'),
    path('osoby/<int:pk>/update/', osoba_update, name='osoba-update'),
    path('osoby/<int:pk>/delete/', osoba_delete, name='osoba-delete'),
    path('stanowiska/', stanowisko_view, name='stanowiska-list'),
    path('stanowiska/<int:pk>/', stanowisko_view, name='stanowisko-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
