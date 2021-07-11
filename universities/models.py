from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "universities"

    def __str__(self):
        return self.name
