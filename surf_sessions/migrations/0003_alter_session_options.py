# Generated by Django 5.1.4 on 2024-12-31 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surf_sessions', '0002_alter_session_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['-date', '-time']},
        ),
    ]
