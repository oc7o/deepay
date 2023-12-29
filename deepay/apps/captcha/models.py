from django.db import models

from deepay.models import DefaultModel


class Captcha(DefaultModel):
    """
    Captcha model
    """

    text = models.CharField(max_length=255)

    # expires = models.DateTimeField() # TODO: add expires field
    image = models.ImageField(
        upload_to="uploads/captchas/",
        default="/media/static/defaults/placeholder.png",
    )

    # TODO: Why?
    def create(self, *args, **kwargs):
        self.save(*args, **kwargs)

    def __str__(self):
        return f"{self.web_id} - {self.text}"

    def __unicode__(self):
        return self.captcha

    class Meta:
        db_table = "captcha"
        verbose_name = "Captcha"
        verbose_name_plural = "Captchas"
