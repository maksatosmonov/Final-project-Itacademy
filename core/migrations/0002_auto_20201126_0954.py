# Generated by Django 3.1.3 on 2020-11-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/photos/'),
        ),
    ]
