# Generated by Django 2.1.2 on 2019-05-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageserver', '0002_auto_20190503_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default='unknown', max_length=255),
        ),
    ]
