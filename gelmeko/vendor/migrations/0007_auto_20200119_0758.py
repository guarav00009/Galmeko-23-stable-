# Generated by Django 2.2 on 2020-01-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_auto_20200114_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendoruser',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Active'), (2, 'Rejected'), (3, 'Deleted')], default=0, verbose_name='status'),
        ),
    ]