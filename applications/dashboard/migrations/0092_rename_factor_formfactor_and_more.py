# Generated by Django 4.2.7 on 2023-12-18 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0091_rename_gpu_sync_gpu_sync"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Factor",
            new_name="FormFactor",
        ),
        migrations.RenameField(
            model_name="formfactor",
            old_name="factor",
            new_name="form_factor",
        ),
        migrations.RenameField(
            model_name="motherboard",
            old_name="factor",
            new_name="form_factor",
        ),
        migrations.AlterModelTable(
            name="formfactor",
            table="form_factor",
        ),
    ]
