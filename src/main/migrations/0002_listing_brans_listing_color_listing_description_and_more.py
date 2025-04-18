# Generated by Django 5.2 on 2025-04-18 22:38

import django.db.models.deletion
import main.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
        ("users", "0006_alter_profile_location_alter_profile_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="brans",
            field=models.CharField(
                choices=[
                    ("bmw", "BMW"),
                    ("mercedes benz", "Mercedes Benz"),
                    ("audi", "Audi"),
                    ("subaru", "Subaru"),
                    ("tesla", "Tesla"),
                    ("jaguar", "Jaguar"),
                    ("land rover", "Land Rover"),
                    ("bentley", "Bentley"),
                    ("bugatti", "Bugatti"),
                    ("ferrari", "Ferrari"),
                    ("lamborghini", "Lamborghini"),
                    ("honda", "Honda"),
                    ("toyota", "Toyota"),
                    ("chevrolet", "Chevrolet"),
                    ("porsche", "Porsche"),
                ],
                default=None,
                max_length=24,
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="color",
            field=models.CharField(default="White", max_length=24),
        ),
        migrations.AddField(
            model_name="listing",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="engine",
            field=models.CharField(default="", max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="image",
            field=models.ImageField(default="", upload_to=main.utils.user_listing_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="location",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.location",
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="milage",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="listing",
            name="model",
            field=models.CharField(default="", max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="transmission",
            field=models.CharField(
                choices=[("automatic", "Automatic"), ("manual", "Manual")],
                default=None,
                max_length=24,
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="vin",
            field=models.CharField(default="", max_length=12),
            preserve_default=False,
        ),
    ]
