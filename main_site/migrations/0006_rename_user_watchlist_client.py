# Generated by Django 4.2.6 on 2023-11-30 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0005_alter_watchlist_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='user',
            new_name='client',
        ),
    ]
