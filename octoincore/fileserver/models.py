from django.db import models
from django.utils.translation import gettext as _

from mptt.models import MPTTModel, TreeForeignKey

class Directory(MPTTModel):
    name = models.CharField(max_length=50, name=_("name"))
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


class File(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="fileserver/")

