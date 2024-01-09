# Generated by Django 4.2.7 on 2024-01-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0116_mobile_alter_case_image_alter_cpu_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MobileField",
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
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "mobile_field",
            },
        ),
    ]
