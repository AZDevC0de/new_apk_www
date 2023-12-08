from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Person, Team, Stanowisko
from ..models import Osoba

class OsobaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #  wymagane obiekty dla relacji ForeignKey
        wlasciciel = User.objects.create_user(username='testuser', password='testpassword123')
        stanowisko = Stanowisko.objects.create(nazwa='Developer', opis='Tworzy oprogramowanie.')
        team = Team.objects.create(name='TeamX', country='X')

        # tworze obiekt Osoba z powiązanymi obiektami
        Osoba.objects.create(
            imie='Jan',
            nazwisko='Kowalski',
            plec=2,
            stanowisko=stanowisko,
            team=team,
            wlasciciel=wlasciciel
        )

    def test_imie_label(self):
        # Pobieram\osobę, którą utworzyliśmy w setUpTestData
        osoba = Osoba.objects.get(id=1)
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_nazwisko_max_length(self):
        osoba = Osoba.objects.get(id=1)
        max_length = osoba._meta.get_field('nazwisko').max_length
        self.assertEqual(max_length, 70)

# class PersonModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         Person.objects.create(name='Jan', shirt_size='L')
#
#     def test_first_name_label(self):
#         person = Person.objects.get(id=1)
#         field_label = person._meta.get_field('name').verbose_name
#         self.assertEqual(field_label, 'name')
#
#     def test_first_name_max_length(self):
#         person = Person.objects.get(id=1)
#         max_length = person._meta.get_field('name').max_length
#         self.assertEqual(max_length, 60)
# class PersonModelTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         Person.objects.create(name='Jan', shirt_size='L')
#         Person.objects.create(name='Anna', shirt_size='M')
#
#     def test_person_ids(self):
#         person1 = Person.objects.get(name='Jan')
#         person2 = Person.objects.get(name='Anna')
#         self.assertNotEqual(person1.id, person2.id)

class TeamModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Team.objects.create(name='Team1', country='PL')
        Team.objects.create(name='Team2', country='US')

    def test_team_ids(self):
        team1 = Team.objects.get(name='Team1')
        team2 = Team.objects.get(name='Team2')
        self.assertNotEqual(team1.id, team2.id)