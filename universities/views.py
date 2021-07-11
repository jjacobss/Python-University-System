from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
import csv
from .models import University
from students.models import Student
from departments.models import Department
from .forms import UniversityForm

# Create your views here.
def index(request):
    """The home page for the university system"""
    return render(request, 'universities/index.html')

@login_required
def universities(request):
    """Show all universities"""
    universities = University.objects.filter(owner=request.user).order_by('name')
    context = {'universities': universities}
    return render(request, 'universities/universities.html', context)


@login_required
def university(request, university_id):
    """Show a specific university"""
    uni = University.objects.get(id=university_id)
    # Check to make sure the university belongs to the current user
    if uni.owner != request.user:
        raise Http404
    departments = Department.objects.filter(university=uni)
    students = []
    for dept in departments:
        if Student.objects.filter(major_department=dept):
            student = Student.objects.filter(major_department=dept).values()
            students.append(student)
    context = {'uni': uni, 'students': students, 'departments': departments}
    return render(request, 'universities/university.html', context)


@login_required
def new_university(request):
    """Add a new university"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = UniversityForm
    else:
        # POST data submitted; process data
        form = UniversityForm(data=request.POST)
        if form.is_valid():
            new_university = form.save(commit=False)
            new_university.owner = request.user
            new_university.save()
            return redirect('universities:universities')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'universities/new_university.html', context)


@login_required
def edit_university(request, university_id):
    """Edit an existing university"""
    university = University.objects.get(id=university_id)
    # Check to make sure the university is owned by the user
    if university.owner != request.user:
        raise Http404
    name = university.name

    if request.method != 'POST':
        # initial request; pre-fill form with current entry
        form = UniversityForm(instance=university)
    else:
        # POST data submitted, process data
        form = UniversityForm(instance=university, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('universities:university', university_id=university.id)

    context = {'university': university, 'name': name, 'form': form}
    return render(request, 'universities/edit_university.html', context)


@login_required
def delete_university(request, university_id):
    university = University.objects.get(id=university_id)
    # Check to make sure the university is owned by the user
    if university.owner != request.user:
        raise Http404
    # BA-LETED
    University.objects.get(id=university_id).delete()
    # After delete, redirect back to main universities page
    universities = University.objects.filter(owner=request.user).order_by('name')
    context = {'universities': universities}
    return render(request, 'universities/universities.html', context)


@login_required
def export_university(request, university_id):
    uni = University.objects.get(id=university_id)
    filename = uni.name + "_export.csv"
    departments = Department.objects.filter(university=uni)
    students = []
    try:
        with open(filename, 'w', newline='\n') as f:
            csv_writer = csv.writer(f, delimiter=",")
            csv_writer.writerow(["Department", "Student Name", "Email", "Major", "Year", "Date Enrolled"])
            for dept in departments:
                if Student.objects.filter(major_department=dept):
                    students.append(Student.objects.filter(major_department=dept).values())
                    for student in Student.objects.filter(major_department=dept):
                        csv_writer.writerow([dept.name, student.name, student.email, student.major,
                                             student.year_in_school, student.date_enrolled])
        messages.success(request, 'Successfully Exported the University!')
    except Exception as e:
        print(f"Error while exporting university file: {e}")

    context = {'uni': uni, 'students': students, 'departments': departments}
    return render(request, 'universities/university.html', context)
