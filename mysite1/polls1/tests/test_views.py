from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Osoba, Stanowisko, Team
from datetime import date


class OsobaDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #  obiekty powiązane z osoba
        stanowisko = Stanowisko.objects.create(nazwa='Programista', opis='Opis stanowiska')
        team = Team.objects.create(name='TeamName', country='PL')
        wlasciciel = User.objects.create_user(username='testuser', password='12345')

        # Utwórz Osoba
        Osoba.objects.create(
            imie='Jan',
            nazwisko='Kowalski',
            plec=1,
            stanowisko=stanowisko,
            data_dodania=date.today(),
            team=team,
            wlasciciel=wlasciciel
        )

    def test_view_url_accessible_by_name(self):
        # Logowanie autoryzacja
        self.client.login(username='testuser', password='12345')

        #get reverse do zbudowania URL-a na podstawie nazwy i przekazuje ID pierwszej osoby jako argument
        response = self.client.get(reverse('osoba-detail', args=[1]))
        self.assertEqual(response.status_code, 200)
