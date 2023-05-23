# Generated by Django 4.2 on 2023-05-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0016_alter_activity_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityuser',
            name='participate_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Wait-listed', 'Wait-listed'), ('Rejected', 'Rejected')], default='Wait-listed', max_length=20),
        ),
    ]
