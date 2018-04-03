from django.db import models


class Page(models.Model):
    url = models.CharField("URL", max_length=256, null=False, blank=False)
