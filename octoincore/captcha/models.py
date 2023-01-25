from django.db import models


class Captcha(models.Model):
    """
    Captcha model
    """

    captcha = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    web_id = models.CharField(max_length=255, unique=True)

    # expires = models.DateTimeField()
    image = models.ImageField(
        upload_to="uploads/captchas/", default="defaults/placeholder.png",
    )

    def create(self, *args, **kwargs):
        self.save(*args, **kwargs)

    def __unicode__(self):
        return self.captcha

    class Meta:
        db_table = "captcha"
        verbose_name = "Captcha"
        verbose_name_plural = "Captchas"

