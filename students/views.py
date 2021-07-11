from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Student
from .forms import StudentForm


# Create your views here.
@login_required
def students(request):
    """Show all students"""
    students = Student.objects.filter(owner=request.user).order_by('name')
    context = {'students': students}
    return render(request, 'students/students.html', context)


@login_required
def student(request, student_id):
    """Show details on a specific student"""
    student = Student.objects.get(id=student_id)
    # Check to make sure the student belongs to the current user
    if student.owner != request.user:
        raise Http404
    context = {'student': student}
    return render(request, 'students/student.html', context)


@login_required
def new_student(request):
    """Add a new student"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = StudentForm
    else:
        # POST data submitted; process data
        form = StudentForm(data=request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.owner = request.user
            new_student.save()
            return redirect('students:students')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'students/new_student.html', context)


@login_required
def edit_student(request, student_id):
    """Edit an existing student"""
    student = Student.objects.get(id=student_id)
    # Check to make sure the student is owned by the user
    if student.owner != request.user:
        raise Http404
    name = student.name
    email = student.email
    major = student.major
    year_in_school = student.year_in_school
    date_enrolled = student.date_enrolled
    major_department = student.major_department

    if request.method != 'POST':
        # initial request; pre-fill form with current entry
        form = StudentForm(instance=student)
    else:
        # POST data submitted, process data
        form = StudentForm(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student', student_id=student.id)

    context = {'student': student, 'name': name, 'email': email, 'major': major, 'year_in_school': year_in_school,
               'date_enrolled': date_enrolled, 'major_department': major_department, 'form': form}
    return render(request, 'students/edit_student.html', context)


@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    # Check to make sure the student is owned by the user
    if student.owner != request.user:
        raise Http404
    # BA-LETED
    Student.objects.get(id=student_id).delete()
    # After delete, redirect back to main students page
    students = Student.objects.filter(owner=request.user).order_by('name')
    context = {'students': students}
    return render(request, 'students/students.html', context)
