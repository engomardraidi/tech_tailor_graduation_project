# Generated by Django 4.2.7 on 2023-12-18 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0083_factor_motherboard_factor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="motherboard",
            name="from_factor",
        ),
    ]