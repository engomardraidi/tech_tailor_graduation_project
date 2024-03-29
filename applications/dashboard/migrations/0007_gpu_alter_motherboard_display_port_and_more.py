# Generated by Django 4.2.7 on 2023-11-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0006_rename_form_factor_motherboard_from_factor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gpu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("pci_e", models.FloatField()),
                ("series", models.CharField(max_length=50)),
                ("vram", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("producer", models.CharField(max_length=100)),
                ("length", models.FloatField()),
                ("slots", models.FloatField()),
                ("connectors_8pin", models.PositiveIntegerField()),
                ("connectors_6pin", models.PositiveIntegerField()),
                ("hdmi", models.BooleanField()),
                ("display_port", models.BooleanField()),
                ("dvi", models.BooleanField()),
                ("vga", models.BooleanField()),
                ("boost_clock", models.PositiveIntegerField()),
                ("memory_clock", models.PositiveIntegerField()),
                ("sync", models.CharField(max_length=50, null=True)),
                ("tdp", models.PositiveIntegerField()),
                ("url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="display_port",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="dvi",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="hdmi",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="m2_pci_e_3",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="m2_pci_e_4",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="usb_3_headers",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="usb_3_slots",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="usb_3_type_c",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="vga",
            field=models.BooleanField(default=False),
        ),
    ]
