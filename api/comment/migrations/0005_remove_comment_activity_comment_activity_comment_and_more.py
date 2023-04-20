# Generated by Django 4.2 on 2023-04-20 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0011_alter_activity_address'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0004_alter_comment_activity_alter_comment_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='activity',
        ),
        migrations.AddField(
            model_name='comment',
            name='activity_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_comment', to='activity.activity'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
