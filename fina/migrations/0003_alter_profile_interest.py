# Generated by Django 3.2.8 on 2021-10-31 15:13

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fina', '0002_auto_20211031_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interest',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Historical', 'Historical'), ('Biography', 'Biography'), ('Self-Development', 'Self-Development'), ('Business', 'Business')], max_length=66, null=True),
        ),
    ]
