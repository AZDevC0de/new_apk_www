from rest_framework import serializers
from .models import Person,Team, SHIRT_SIZES,MONTHS
from django.utils import timezone
from .models import Osoba,Stanowisko

class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'
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

class OsobaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Osoba
        fields = ['imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']







    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Imię może zawierać tylko litery.")
        return value

    def validate_data_dodania(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Data dodania nie może być z przyszłości.")
        return value

