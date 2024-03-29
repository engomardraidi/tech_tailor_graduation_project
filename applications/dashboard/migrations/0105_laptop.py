# Generated by Django 4.2.7 on 2023-12-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0104_rename_image_url_case_external_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Laptop",
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
                ("name", models.CharField(max_length=255)),
                ("screen_size", models.FloatField()),
                ("cpu_type", models.CharField(max_length=255)),
                ("memory", models.PositiveIntegerField()),
                ("storage", models.CharField(max_length=255)),
                ("gpu", models.CharField(max_length=255)),
                ("resolution", models.CharField(max_length=255)),
                ("weight", models.FloatField()),
                ("backlit_keyboard", models.BooleanField(default=False)),
                ("touchscreen", models.BooleanField(default=False)),
                ("cpu_speed", models.FloatField()),
                ("number_of_cores", models.PositiveIntegerField()),
                ("display_type", models.CharField(max_length=255)),
                ("graphic_type", models.CharField(max_length=255)),
                ("operating_system", models.CharField(max_length=255)),
                ("webcam", models.BooleanField(default=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("use", models.CharField(max_length=255)),
                ("external_image", models.URLField(null=True)),
                ("image", models.ImageField(null=True, upload_to="images/laptops/")),
            ],
            options={
                "db_table": "laptop",
            },
        ),
    ]
