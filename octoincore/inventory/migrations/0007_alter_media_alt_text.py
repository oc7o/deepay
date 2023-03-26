# Generated by Django 4.1 on 2023-03-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0006_alter_productinventory_brand_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="alt_text",
            field=models.CharField(
                blank=True,
                help_text="format: required, max-255",
                max_length=255,
                null=True,
                verbose_name="alternative text",
            ),
        ),
    ]
