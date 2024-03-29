# Generated by Django 4.2.7 on 2023-12-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0061_alter_case_color"),
    ]

    operations = [
        migrations.CreateModel(
            name="CaseSidePanel",
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
                ("side_panel", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "case_side_panel",
            },
        ),
    ]
