# Generated by Django 3.1.5 on 2021-01-25 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20210125_0147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='year_of_birtday',
            new_name='year_of_birthday',
        ),
    ]
