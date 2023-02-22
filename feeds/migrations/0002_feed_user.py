# Generated by Django 4.1.7 on 2023-02-22 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
