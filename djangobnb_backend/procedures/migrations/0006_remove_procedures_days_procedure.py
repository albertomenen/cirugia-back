# Generated by Django 5.0.2 on 2024-04-04 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procedures', '0005_rename_guest_reservation_guests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedures',
            name='days_procedure',
        ),
    ]
