# Generated by Django 4.2.7 on 2024-01-15 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "dashboard",
            "0124_alter_motherboard_display_port_alter_motherboard_dvi_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="motherboard",
            name="hdmi",
            field=models.PositiveIntegerField(),
        ),
    ]