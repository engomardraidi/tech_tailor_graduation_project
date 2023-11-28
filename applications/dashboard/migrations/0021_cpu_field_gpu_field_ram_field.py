# Generated by Django 4.2.7 on 2023-11-27 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0020_remove_pcparts_cpu_remove_pcparts_gpu_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cpu",
            name="field",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cpus",
                to="dashboard.field",
            ),
        ),
        migrations.AddField(
            model_name="gpu",
            name="field",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="gpus",
                to="dashboard.field",
            ),
        ),
        migrations.AddField(
            model_name="ram",
            name="field",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rams",
                to="dashboard.field",
            ),
        ),
    ]