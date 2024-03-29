# Generated by Django 4.2.7 on 2023-11-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0004_cpu"),
    ]

    operations = [
        migrations.CreateModel(
            name="Motherboard",
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
                ("form_factor", models.CharField(max_length=50)),
                ("socket", models.CharField(max_length=50)),
                ("memory_type", models.CharField(max_length=50)),
                ("memory_max_capacity", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("chipset", models.CharField(max_length=50)),
                ("producer", models.CharField(max_length=100)),
                ("ram_slots", models.PositiveIntegerField()),
                ("m2_pci_e_3", models.PositiveIntegerField()),
                ("m2_pci_e_4", models.PositiveIntegerField()),
                ("usb_3_slots", models.PositiveIntegerField()),
                ("usb_3_headers", models.PositiveIntegerField()),
                ("usb_3_type_c", models.PositiveIntegerField()),
                ("vga", models.BooleanField()),
                ("dvi", models.BooleanField()),
                ("display_port", models.BooleanField()),
                ("hdmi", models.BooleanField()),
                ("pci_e_3", models.PositiveIntegerField()),
                ("pci_e_4", models.PositiveIntegerField()),
                ("url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "motherboard",
            },
        ),
        migrations.AlterField(
            model_name="cpu",
            name="status",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="ram",
            name="status",
            field=models.BooleanField(default=True),
        ),
    ]
