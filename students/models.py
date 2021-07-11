import sys
sys.path.append("..")
from django.db import models
from django.contrib.auth.models import User
from classes.models import Class
from departments.models import Department


# Create your models here.
class Student(models.Model):
    """A student object to hold student information"""
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    date_enrolled = models.DateField(auto_now_add=False)
    major_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name.capitalize()} - {self.year_in_school} - {self.major}"
