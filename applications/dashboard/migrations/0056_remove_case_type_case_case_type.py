# Generated by Django 4.2.7 on 2023-12-10 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0055_case_casetype"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="case",
            name="type",
        ),
        migrations.AddField(
            model_name="case",
            name="case_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.casetype",
            ),
        ),
    ]
