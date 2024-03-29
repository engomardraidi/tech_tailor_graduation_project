# Generated by Django 4.2.7 on 2023-12-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0105_laptop"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="laptop",
            name="external_image",
        ),
        migrations.AddField(
            model_name="laptop",
            name="gpu_cores",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="laptop",
            name="gpu_speed",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="laptop",
            name="vram",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="laptop",
            name="number_of_cores",
            field=models.CharField(max_length=50),
        ),
    ]
