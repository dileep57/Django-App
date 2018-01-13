# Generated by Django 2.0.1 on 2018-01-12 16:09

import DileepImage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DileepImage', '0007_auto_20180112_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='albummodel',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to=DileepImage.models.location),
        ),
    ]
