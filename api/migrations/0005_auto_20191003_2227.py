# Generated by Django 2.2.1 on 2019-10-03 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191003_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.DateField(blank=True),
        ),
    ]
