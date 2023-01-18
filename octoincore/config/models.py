from django.db import models

class ServerSettings(models.Model):
    attribute = models.CharField(max_length=4095)
    value = models.CharField(max_length=4095)