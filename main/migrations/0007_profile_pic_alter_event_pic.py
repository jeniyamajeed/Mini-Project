# Generated by Django 4.1.2 on 2022-11-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_profile_email_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='test', upload_to='profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='pic',
            field=models.ImageField(upload_to='events'),
        ),
    ]
