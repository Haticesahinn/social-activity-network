# Generated by Django 4.2 on 2023-04-11 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('userprofile', '0002_alter_profile_follower_alter_profile_following_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
    ]
