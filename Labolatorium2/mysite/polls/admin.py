from django.contrib import admin

from .models import Question

# from .models import Question, Person
# # Register your models here.
#
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ('name', 'country')
#
#
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'shirt_size', 'month_added', 'team')
#     list_filter = ('shirt_size', 'month_added', 'team')
#
# admin.site.register(Team, TeamAdmin)
# admin.site.register(Person, PersonAdmin)
admin.site.register(Question)