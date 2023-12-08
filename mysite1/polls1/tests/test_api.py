from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from ..models import Osoba, Stanowisko, Team

class OsobaAPITests(APITestCase):

    def setUp(self):
        # użytkownik i token
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # obiekty Stanowisko i Team
        self.stanowisko = Stanowisko.objects.create(nazwa='Programista', opis='Tworzy kod.')
        self.team = Team.objects.create(name='Zespół', country='PL')

    def test_create_osoba(self):
        #  do utworzenia obiektu Osoba
        data = {
            'imie': 'Jan',
            'nazwisko': 'Kowalski',
            'plec': 2,
            'stanowisko': self.stanowisko.id,
            'team': self.team.id
        }
        response = self.client.post(reverse('osoba-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Osoba.objects.count(), 1)
        self.assertEqual(Osoba.objects.get().imie, 'Jan')

    def test_list_osoba(self):
        # Stwórz obiekt Osoba
        Osoba.objects.create(
            imie='Anna',
            nazwisko='Nowak',
            plec=1,
            stanowisko=self.stanowisko,
            team=self.team,
            wlasciciel=self.user
        )
        response = self.client.get(reverse('osoba-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['imie'], 'Anna')
