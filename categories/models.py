from django.db import models

from core.models import TimeStampedUUIDModel


class Category(TimeStampedUUIDModel):
    name = models.CharField(max_length=255, unique=True,error_messages={"unique":"نام تکراری است"})
    description = models.TextField(blank=True, default="")
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta(TimeStampedUUIDModel.Meta):
        db_table = "categories"
        verbose_name_plural = "categories"
