from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'major', 'year_in_school', 'date_enrolled', 'major_department']
        labels = {'name': 'Name', 'email': 'Email', 'major': 'Major', 'year_in_school': 'Year in school',
                  'date_enrolled': 'Date enrolled (YYYY-MM-DD)', 'major_department': 'Major department'}

