# Generated by Django 2.0.1 on 2018-01-12 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DileepImage', '0005_auto_20180112_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DileepImage.AlbumModel'),
        ),
    ]
