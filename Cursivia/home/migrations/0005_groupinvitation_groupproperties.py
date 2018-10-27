# Generated by Django 2.1 on 2018-10-26 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('home', '0004_auto_20181025_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_invited', models.DateTimeField(default=django.utils.timezone.now)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='auth.Group')),
                ('invited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_invitations', to=settings.AUTH_USER_MODEL)),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_members', models.BooleanField(default=False)),
                ('admins', models.ManyToManyField(related_name='admin_of', to=settings.AUTH_USER_MODEL)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='auth.Group')),
            ],
        ),
    ]
