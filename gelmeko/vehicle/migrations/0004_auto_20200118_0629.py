# Generated by Django 2.2 on 2020-01-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_auto_20200118_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (2, 'Booked'), (3, 'Deleted')], default=1, verbose_name='status'),
        ),
    ]
