# Generated by Django 2.2.5 on 2020-02-14 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='permission',
        ),
    ]
