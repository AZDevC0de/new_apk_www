# Generated by Django 4.2.7 on 2023-11-17 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls1', '0008_osoba_team_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='datetime_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
