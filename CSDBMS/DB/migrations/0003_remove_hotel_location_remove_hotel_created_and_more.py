# Generated by Django 4.2.1 on 2023-05-30 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0002_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='created',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='image',
        ),
    ]
