# Generated by Django 2.1 on 2018-10-25 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181025_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupinvitation',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupinvitation',
            name='invited_by',
        ),
        migrations.RemoveField(
            model_name='groupinvitation',
            name='invitee',
        ),
        migrations.RemoveField(
            model_name='groupproperties',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='groupproperties',
            name='group',
        ),
        migrations.DeleteModel(
            name='GroupInvitation',
        ),
        migrations.DeleteModel(
            name='GroupProperties',
        ),
    ]
