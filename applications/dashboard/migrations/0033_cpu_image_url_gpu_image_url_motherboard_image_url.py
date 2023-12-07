# Generated by Django 4.2.7 on 2023-12-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0032_ram_image_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="cpu",
            name="image_url",
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="gpu",
            name="image_url",
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="motherboard",
            name="image_url",
            field=models.URLField(null=True),
        ),
    ]