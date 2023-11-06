from django.contrib import admin
from .models import Osoba, Person
from .models import Stanowisko

# Register your models here.
# admin.site.register(Osoba)
# admin.site.register(Stanowisko)
# admin.site.register(OsobaAdmin)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['']
#     list_filter = ['']
#     readonly_fields = ['data_dodania']
@admin.register(Osoba)
class OsobaData(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)
    list_filter = ('plec', 'stanowisko','data_dodania')
    search_fields = ['imie', 'nazwisko']
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']

    @admin.display(description='Stanowisko (id)')
    def display_stanowisko(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"
class PersonAdmin(admin.ModelAdmin):
    # zmienna list_display przechowuje listę pól, które mają się wyświetlać w widoku listy danego modelu w panelu administracynym
    list_display = ['name', 'shirt_size']
# class OsobaAdmin(admin.ModelAdmin):
#     list_filter = ('plec', 'stanowisko')
#     search_fields = ['imie', 'nazwisko']
#     readonly_fields = ('data_dodania',)

    @admin.display(description='Pełne imię i nazwisko')
    def full_name(self, obj):
        return f"{obj.imie} {obj.nazwisko}"

    # actions = ['zmien_stanowisko']

    # def zmien_stanowisko(self, request, queryset):
    #     # logika zmiany stanowiska
    #     ...

    # zmien_stanowisko.short_description = "Zmień stanowisko wybranych osób"
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    list_filter = ('nazwa',)


# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Person, PersonAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)
