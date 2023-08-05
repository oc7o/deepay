import uuid

from django.db import models


class DefaultModel(models.Model):
    """Base model for all models in deepay."""

    class Meta:
        abstract = True

    web_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the string representation of the model."""
        return f"{self.web_id}"
