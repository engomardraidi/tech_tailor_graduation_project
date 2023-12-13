# Generated by Django 4.2.7 on 2023-12-12 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0071_field_case_budget_field_internal_drive_budget_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CPUSocket",
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
                ("socket", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("staus", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "cpu_socket",
            },
        ),
        migrations.AddField(
            model_name="cpu",
            name="cpu_socket",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.cpusocket",
            ),
        ),
        migrations.AddField(
            model_name="motherboard",
            name="cpu_socket",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.cpusocket",
            ),
        ),
    ]