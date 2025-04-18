# Generated by Django 5.2 on 2025-04-15 15:32

import localflavor.us.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_location_district_location_postal_code_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="location",
            name="postal_code",
        ),
        migrations.AddField(
            model_name="location",
            name="Zip_Code",
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="location",
            name="District",
            field=localflavor.us.models.USStateField(default="NY", max_length=2),
        ),
    ]
