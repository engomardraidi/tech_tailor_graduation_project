# Generated by Django 4.2.7 on 2023-12-11 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0068_alter_drivetype_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="PowerSupplyEfficiency",
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
                ("efficiency", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "power_supply_efficiency",
            },
        ),
        migrations.CreateModel(
            name="PowerSupplyType",
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
                ("type", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "power_supply_type",
            },
        ),
        migrations.CreateModel(
            name="PowerSupply",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("wattage", models.PositiveIntegerField()),
                ("image_url", models.URLField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "efficiency",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.powersupplyefficiency",
                    ),
                ),
                (
                    "power_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.powersupplytype",
                    ),
                ),
            ],
            options={
                "db_table": "power_supply",
            },
        ),
    ]
