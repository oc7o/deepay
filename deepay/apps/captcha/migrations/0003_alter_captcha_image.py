# Generated by Django 4.2.4 on 2023-12-28 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captcha', '0002_alter_captcha_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captcha',
            name='image',
            field=models.ImageField(default='/media/static/defaults/placeholder.png', upload_to='uploads/captchas/'),
        ),
    ]
