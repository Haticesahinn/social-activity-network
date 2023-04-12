# Generated by Django 4.2 on 2023-04-11 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userprofile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("about", models.TextField(blank=True, max_length=600, null=True)),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("is_online", models.BooleanField(default=False)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "education_level",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ES", "Elementary School"),
                            ("MS", "Middle School"),
                            ("HS", "High School"),
                            ("AD", "Associate's Degree"),
                            ("BD", "Bachelor's Degree"),
                            ("MD", "Master's Degree"),
                            ("PhD", "Doctorate or PhD"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_modified_at", models.DateTimeField(auto_now=True)),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="/default.png",
                        null=True,
                        upload_to=userprofile.models.low_file_directory_path,
                    ),
                ),
                ("company_url", models.URLField(blank=True, null=True)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "follower",
                    models.ManyToManyField(
                        blank=True, related_name="follower", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "following",
                    models.ManyToManyField(
                        blank=True,
                        related_name="following",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
                "db_table": "profile",
            },
        ),
    ]