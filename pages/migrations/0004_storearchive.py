# Generated by Django 3.2.7 on 2021-11-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_archiveaudio_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
