from django.db import models

# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Teams"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} ({self.shirt_size})"



class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=50, blank=False)
    opis = models.TextField(default="")

    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name_plural = "Stanowisko"

class Plec(models.IntegerChoices):
    KOBIETA = 1, 'Kobieta'
    MEZCZYZNA = 2, 'Mężczyzna'
    INNE = 3, 'Inne'
class Osoba(models.Model):
    # lista wartości do wyboru w formie krotek
    # SHIRT_SIZES = (
    #     ('K', 'Kobieta'),
    #     ('M', 'Mezczyzna'),
    #
    # )
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=70)
    # wskazanie listy poprzez przypisanie do parametru choices
    # plec = models.CharField(max_length=1, choices=SHIRT_SIZES)
    plec = models.IntegerField(choices=Plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):

        return f"{self.imie} {self.nazwisko}"

    class Meta:
        verbose_name_plural = "Osoby"
        ordering = ["nazwisko"]

