# Generated by Django 2.1 on 2018-11-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_groupproperties_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupproperties',
            name='state',
            field=models.CharField(blank=True, choices=[('p', 'Publicado'), ('b', 'Borrador'), ('d', 'Denunciado'), ('e', 'Eliminado')], default='b', help_text='situacion actual de la publicacion', max_length=1),
        ),
    ]
