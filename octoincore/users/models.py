from email.policy import default

from django.contrib.auth.models import AbstractUser
from django.db import models


class ExtendUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    profile_image = models.ImageField(upload_to="uploads/profile_images/", blank=True, null=True, default="defaults/profile_image.png")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
