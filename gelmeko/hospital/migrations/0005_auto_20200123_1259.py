# Generated by Django 2.2.1 on 2020-01-23 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20200118_1221'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HospitalUser',
            new_name='Hospital',
        ),
    ]
