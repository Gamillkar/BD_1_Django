# Generated by Django 3.1.1 on 2020-09-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20200908_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=2),
        ),
    ]
