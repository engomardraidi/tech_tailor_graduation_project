# Generated by Django 4.2.7 on 2023-12-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0065_case_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="case",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
