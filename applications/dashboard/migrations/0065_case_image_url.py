# Generated by Django 4.2.7 on 2023-12-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0064_case_created_at_case_status_case_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="image_url",
            field=models.URLField(null=True),
        ),
    ]
