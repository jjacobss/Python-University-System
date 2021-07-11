"""Defines URL patterns for students"""

from django.urls import path

from . import views

app_name = "students"
urlpatterns = [
    # Page that shows all students
    path('', views.students, name='students'),
    # Detail page for a single student
    path('students/<int:student_id>/', views.student, name='student'),
    # Page for adding a new student
    path('new_student/', views.new_student, name='new_student'),
    # Page for editing a university
    path('edit_student/<int:student_id>/', views.edit_student, name="edit_student"),
    # Page for deleting a student
    path('delete_student/<int:student_id>/', views.delete_student, name="delete_student"),
]
