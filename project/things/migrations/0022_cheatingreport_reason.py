# Generated by Django 3.0.5 on 2020-04-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0021_auto_20200428_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheatingreport',
            name='reason',
            field=models.CharField(default='No reason', max_length=1024),
        ),
    ]
