# Generated by Django 2.2.12 on 2020-05-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/component/images/banner/'),
        ),
    ]