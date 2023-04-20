# Generated by Django 4.2 on 2023-04-20 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_alter_activity_options_alter_activity_table'),
        ('confirmation', '0002_alter_confirmation_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmation',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.activity'),
        ),
    ]
