# Generated by Django 3.0.2 on 2020-01-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20200114_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitaluser',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Active'), (2, 'Rejected'), (3, 'Other')], default=0, verbose_name='status'),
        ),
    ]
