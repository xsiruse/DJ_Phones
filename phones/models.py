from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=64)
    image = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField(default=None, null=True)
    slug = models.CharField(max_length=64, default=None, null=True)

