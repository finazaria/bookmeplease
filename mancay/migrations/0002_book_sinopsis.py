# Generated by Django 3.2.8 on 2021-11-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mancay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Sinopsis',
            field=models.TextField(blank=True, null=True),
        ),
    ]