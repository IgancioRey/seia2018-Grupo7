# Generated by Django 2.1 on 2018-11-05 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0019_denuncia_grupodenunciado'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado_grupo',
            name='admins',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
