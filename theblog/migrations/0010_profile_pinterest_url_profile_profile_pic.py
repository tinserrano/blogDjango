# Generated by Django 4.0.4 on 2022-04-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pinterest_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
