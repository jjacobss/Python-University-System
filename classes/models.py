import sys
sys.path.append("..")
from django.db import models
from departments.models import Department


# Create your models here.
class Class(models.Model):
    """Classes students are registered for"""
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "classes"

    def __str__(self):
        """Returns a string representation of the class"""
        return f"{self.name} offered by the {self.department.name} Department"
