"""Defines URL patterns for universities"""

from django.urls import path

from . import views

app_name = "universities"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all Universities
    path('universities/', views.universities, name='universities'),
    # Detail page for a single university
    path('universities/<int:university_id>/', views.university, name='university'),
    # Page for adding a new university
    path('new_university/', views.new_university, name='new_university'),
    # Page for editing a university
    path('edit_university/<int:university_id>/', views.edit_university, name="edit_university"),
    # Page for deleting a university
    path('delete_university/<int:university_id>/', views.delete_university, name="delete_university"),
    # Page for exporting a university to csv
    path('export_university/<int:university_id>/', views.export_university, name="export_university"),
]
