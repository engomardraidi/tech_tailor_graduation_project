# Generated by Django 4.2.7 on 2023-11-26 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0011_pc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pc",
            name="cpu",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PCs",
                to="dashboard.cpu",
            ),
        ),
    ]
