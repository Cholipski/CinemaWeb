# Generated by Django 3.1.5 on 2021-01-24 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20210124_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='user',
            new_name='client',
        ),
    ]