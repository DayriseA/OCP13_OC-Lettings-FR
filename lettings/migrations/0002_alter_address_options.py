# Generated by Django 5.0.6 on 2024-05-15 05:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "Addresses"},
        ),
    ]