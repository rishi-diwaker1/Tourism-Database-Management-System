# Generated by Django 4.2.1 on 2023-05-30 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0003_remove_hotel_location_remove_hotel_created_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
