"""Defines URL patterns for departments"""

from django.urls import path

from . import views

app_name = "departments"
urlpatterns = [
    # Page that shows all departments
    path('', views.departments, name='departments'),
    # Detail page for a single department
    path('departments/<int:department_id>/', views.department, name='department'),
    # Page for adding a new department
    path('new_department/', views.new_department, name='new_department'),
    # Page for editing a department
    path('edit_department/<int:department_id>/', views.edit_department, name="edit_department"),
    # Page for deleting a department
    path('delete_department/<int:department_id>/', views.delete_department, name="delete_department"),
]
