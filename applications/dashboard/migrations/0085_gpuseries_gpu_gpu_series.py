# Generated by Django 4.2.7 on 2023-12-18 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0084_remove_motherboard_from_factor"),
    ]

    operations = [
        migrations.CreateModel(
            name="GPUSeries",
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
                ("series", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "db_table": "gpu_series",
            },
        ),
        migrations.AddField(
            model_name="gpu",
            name="gpu_series",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.gpuseries",
            ),
        ),
    ]