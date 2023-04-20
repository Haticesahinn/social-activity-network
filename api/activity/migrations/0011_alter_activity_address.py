# Generated by Django 4.2 on 2023-04-20 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('activity', '0010_alter_activity_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='address.address'),
        ),
    ]
