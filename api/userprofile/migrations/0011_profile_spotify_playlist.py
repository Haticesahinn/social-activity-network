# Generated by Django 4.2 on 2023-06-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_alter_profile_follower_alter_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='spotify_playlist',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
