# Generated by Django 2.2.1 on 2019-10-03 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_profile_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='limit',
            field=models.IntegerField(blank=True),
        ),
    ]
