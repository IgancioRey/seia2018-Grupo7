# Generated by Django 2.1 on 2018-08-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='createDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='postDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]