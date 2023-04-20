# Generated by Django 4.2 on 2023-04-20 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("advertisement", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("confirmation", "0004_alter_confirmation_activity"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvertisementConfirmation",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("confirm_status", models.BooleanField(default=False)),
                (
                    "confirm_type",
                    models.CharField(
                        blank=True,
                        choices=[("Create", "Create"), ("Update", "Update")],
                        max_length=8,
                        null=True,
                    ),
                ),
                (
                    "advertisement",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="advertisement",
                        to="advertisement.advertisement",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]