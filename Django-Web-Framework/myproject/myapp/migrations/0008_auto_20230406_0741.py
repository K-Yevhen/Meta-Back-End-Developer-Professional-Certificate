# Generated by Django 3.2.5 on 2023-04-06 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_menu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
