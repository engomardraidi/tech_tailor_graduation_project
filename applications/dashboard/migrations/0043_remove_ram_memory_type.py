# Generated by Django 4.2.7 on 2023-12-08 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0042_ram_ram_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ram",
            name="memory_type",
        ),
    ]