# Generated by Django 4.2.7 on 2023-12-18 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0088_rename_gpu_series_gpu_series"),
    ]

    operations = [
        migrations.CreateModel(
            name="GPUSync",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                ("sync", models.CharField(max_length=50, null=True)),
            ],
            options={
                "db_table": "gpu_sync",
            },
        ),
        migrations.AddField(
            model_name="gpu",
            name="gpu_sync",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.gpusync",
            ),
        ),
    ]