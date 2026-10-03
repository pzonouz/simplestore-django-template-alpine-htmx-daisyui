from django.db import models

from core.models import TimeStampedUUIDModel


class Product(TimeStampedUUIDModel):
    name = models.TextField()

    class Meta(TimeStampedUUIDModel.Meta):
        db_table = "products"
