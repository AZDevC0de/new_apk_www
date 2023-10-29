>>> from polls1.models import Osoba, Stanowisko
>>> osoby = Osoba.objects.all()
>>> print(osoby)
<QuerySet [<Osoba: Angela Kowalska>, <Osoba: Jan Nowak>, <Osoba: Michał Staron>]>

>>> osoba_id_3 = Osoba.objects.get(id=3)
>>> print(osoba_id_3)
Michał Staron

>>> osoby_na_litere = Osoba.objects.filter(nazwisko__startswith='K')
>>> print(osoby_na_litere)
<QuerySet [<Osoba: Angela Kowalska>]>

>>> unikalne_stanowiska = Osoba.objects.values_list('stanowisko__nazwa', flat=True).distinct()
>>> print(unikalne_stanowiska)
<QuerySet ['Księgowa', 'Informatyk', 'Pracownik_fizyczny']>

>>> stanowiska_posortowane = Stanowisko.objects.order_by('-nazwa').values_list('nazwa', flat=True)
>>> print(stanowiska_posortowane)
<QuerySet ['Pracownik_fizyczny', 'Księgowa', 'Informatyk']>

>>> nowa_osoba = Osoba(imie='Jan', nazwisko='Kowalski', plec=Plec.MEZCZYZNA, stanowisko=Stanowisko.objects.get(id=1))
>>> nowa_osoba.save()
>>> print(nowa_osoba)
Jan Kowalski

