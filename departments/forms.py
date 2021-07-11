from django import forms

from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'university']
        labels = {'name': 'Department Name', 'university': 'University Name'}
