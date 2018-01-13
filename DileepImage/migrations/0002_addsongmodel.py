# Generated by Django 2.0.1 on 2018-01-11 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DileepImage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddSongModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(blank=True, max_length=200, null=True)),
                ('song_file', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DileepImage.AlbumModel')),
            ],
        ),
    ]
