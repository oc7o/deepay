# Generated by Django 4.2 on 2023-05-09 10:20

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Captcha",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "web_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(
                        default="defaults/placeholder.png",
                        upload_to="uploads/captchas/",
                    ),
                ),
            ],
            options={
                "verbose_name": "Captcha",
                "verbose_name_plural": "Captchas",
                "db_table": "captcha",
            },
        ),
    ]
