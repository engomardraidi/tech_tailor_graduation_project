# Generated by Django 4.2.7 on 2023-12-18 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0085_gpuseries_gpu_gpu_series"),
    ]

    operations = [
        migrations.AddField(
            model_name="gpuseries",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gpuseries",
            name="status",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="gpuseries",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]