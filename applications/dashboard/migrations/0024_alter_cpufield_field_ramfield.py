# Generated by Django 4.2.7 on 2023-11-28 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0023_alter_cpufield_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cpufield",
            name="field",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.field",
            ),
        ),
        migrations.CreateModel(
            name="RAMField",
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
                ("status", models.BooleanField(default=True)),
                (
                    "field",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.field",
                    ),
                ),
                (
                    "ram",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="dashboard.ram"
                    ),
                ),
            ],
            options={
                "db_table": "ram_field",
            },
        ),
    ]
