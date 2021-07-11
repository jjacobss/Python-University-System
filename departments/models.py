import sys
sys.path.append("..")
from django.db import models
from django.contrib.auth.models import User
from universities.models import University


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a string representation of the department"""
        return f"{self.university.name} {self.name} department"
