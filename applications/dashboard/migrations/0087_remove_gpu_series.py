# Generated by Django 4.2.7 on 2023-12-18 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0086_gpuseries_created_at_gpuseries_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gpu",
            name="series",
        ),
    ]
