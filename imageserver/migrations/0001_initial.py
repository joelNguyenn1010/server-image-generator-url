# Generated by Django 2.1.2 on 2019-05-03 13:28

import datetime
from django.db import migrations, models
import imageserver.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=imageserver.models.image_path)),
                ('date_in_database', models.DateField(default=datetime.date.today, validators=[imageserver.models.validate_image])),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='images',
            name='type',
            field=models.ManyToManyField(blank=True, to='imageserver.Type'),
        ),
    ]
