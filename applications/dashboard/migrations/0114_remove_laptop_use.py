# Generated by Django 4.2.7 on 2023-12-31 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0113_laptopuse"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="laptop",
            name="use",
        ),
    ]