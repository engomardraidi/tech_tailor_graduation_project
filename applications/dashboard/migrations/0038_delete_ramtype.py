# Generated by Django 4.2.7 on 2023-12-08 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0037_alter_ramtype_type"),
    ]

    operations = [
        migrations.DeleteModel(
            name="RamType",
        ),
    ]