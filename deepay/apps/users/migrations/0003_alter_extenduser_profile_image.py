# Generated by Django 4.2.4 on 2023-12-28 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_extenduser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='profile_image',
            field=models.ImageField(blank=True, default='/media/static/defaults/profile_image.png', null=True, upload_to='uploads/profile_images/'),
        ),
    ]
