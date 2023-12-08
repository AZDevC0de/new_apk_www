import graphene
from django.utils.dateparse import parse_date
from graphene_django import DjangoObjectType
from polls1.models import Osoba, Team

# Definicje typów GraphQL dla modeli Django
class OsobaType(DjangoObjectType):
    class Meta:
        model = Osoba
        fields = '__all__'

class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = '__all__'

# Główny typ Query do tworzenia zapytań GraphQL
class Query(graphene.ObjectType):
    # Nowe zapytania
    osoby_by_imie = graphene.List(OsobaType, imie_contains=graphene.String(required=True)) #ozwala znaleźć wszystkie osoby, których imię zawiera podany ciąg znaków.
    osoby_by_date_range = graphene.List(OsobaType, start_date=graphene.String(), end_date=graphene.String())
    #filtrowanie osób dodanych do bazy danych w określonym zakresie dat.
    teams_by_country = graphene.List(TeamType, country=graphene.String(required=True))

    all_osoby = graphene.List(OsobaType)


    osoba_by_id = graphene.Field(OsobaType, id=graphene.Int(required=True))

    all_teams = graphene.List(TeamType)


    team_by_id = graphene.Field(TeamType, id=graphene.Int(required=True))


    osoby_by_nazwisko = graphene.List(OsobaType, nazwisko_contains=graphene.String(required=True))


    def resolve_all_osoby(root, info):
        return Osoba.objects.all()


    def resolve_osoba_by_id(root, info, id):
        try:
            return Osoba.objects.get(pk=id)
        except Osoba.DoesNotExist:
            return None


    def resolve_all_teams(root, info):
        return Team.objects.all()


    def resolve_team_by_id(root, info, id):
        try:
            return Team.objects.get(pk=id)
        except Team.DoesNotExist:
            return None


    def resolve_osoby_by_nazwisko(root, info, nazwisko_contains):
        return Osoba.objects.filter(nazwisko__icontains=nazwisko_contains)

    def resolve_osoby_by_imie(self, info, imie_contains):
        return Osoba.objects.filter(imie__icontains=imie_contains)

    def resolve_osoby_by_date_range(self, info, start_date, end_date):
        start = parse_date(start_date)
        end = parse_date(end_date)
        return Osoba.objects.filter(data_dodania__range=(start, end))

    def resolve_teams_by_country(self, info, country):
        return Team.objects.filter(country__iexact=country)

# schemat
schema = graphene.Schema(query=Query)
