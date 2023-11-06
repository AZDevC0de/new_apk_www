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


//serializers.py
from rest_framework import serializers
from .models import Person,Team, SHIRT_SIZES,MONTHS

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    shirt_size = serializers.ChoiceField(choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True, required=False)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.month_added = validated_data.get('month_added', instance.month_added)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance

# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
python manage.py shell

#importuje modele i serializatory
>>> from polls1.models import Person, Team 
>>> from polls1.serializers import PersonSerializer, TeamSerializer 
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> import io
#tworze nowa instancje klasy Person
>>> person = Person(name='Adam', shirt_size='M', month_added=1)
>>> person.save()
#serializer z nowo utworzoną osobą
>>> serializer = PersonSerializer(person)
>>> print(serializer.data)
{'id': 6, 'name': 'Adam', 'shirt_size': 'M', 'month_added': 1, 'team': None}
>>>
#format JSON
>>> content = JSONRenderer().render(serializer.data)
>>> print(content)
b'{"id":6,"name":"Adam","shirt_size":"M","month_added":1,"team":null}'
#deserializacja
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
#czy są błędy
>>> deserializer = PersonSerializer(data=data)
>>> deserializer.is_valid()
True
>>> print(deserializer.errors)
{}
#jesli dane są poprawne zapisuje sie obiekt
>>> if deserializer.is_valid():
...     new_person = deserializer.save()
...     print(new_person)
...
Adam (M)

