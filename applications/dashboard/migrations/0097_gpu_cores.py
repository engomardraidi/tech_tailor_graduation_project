# Generated by Django 4.2.7 on 2023-12-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0096_ram_timings"),
    ]

    operations = [
        migrations.AddField(
            model_name="gpu",
            name="cores",
            field=models.PositiveIntegerField(null=True),
        ),
    ]