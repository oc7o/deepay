# Generated by Django 4.2.4 on 2023-12-31 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_media_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinventory',
            name='is_default',
            field=models.BooleanField(default=False, help_text='format: true=sub product visible', verbose_name='product default inventory'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='inventory',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stock', to='inventory.productinventory'),
        ),
    ]
