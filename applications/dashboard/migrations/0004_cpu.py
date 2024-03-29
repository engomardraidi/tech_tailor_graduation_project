# Generated by Django 4.2.7 on 2023-11-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0003_alter_ram_timings"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cpu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("socket", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("producer", models.CharField(max_length=100)),
                ("base_clock", models.FloatField(default=0.0)),
                ("turbo_clock", models.FloatField(default=0.0)),
                ("cores", models.PositiveIntegerField()),
                ("threads", models.PositiveIntegerField()),
                ("tdp", models.PositiveIntegerField()),
                ("integrated_graphics", models.CharField(max_length=100)),
                ("url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True, max_length=20)),
            ],
            options={
                "db_table": "cpu",
            },
        ),
    ]
