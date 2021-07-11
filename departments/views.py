from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Department
from students.models import Student
from .forms import DepartmentForm


# Create your views here.
@login_required
def departments(request):
    """Show all departments"""
    departments = Department.objects.filter(owner=request.user).order_by('name')
    context = {'departments': departments}
    return render(request, 'departments/departments.html', context)


@login_required
def department(request, department_id):
    """Show details on a specific department"""
    department = Department.objects.get(id=department_id)
    # Check to make sure the department belongs to the current user
    if department.owner != request.user:
        raise Http404
    students = Student.objects.filter(major_department=department)
    context = {'department': department, 'students': students}
    return render(request, 'departments/department.html', context)


@login_required
def new_department(request):
    """Add a new department"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = DepartmentForm
    else:
        # POST data submitted; process data
        form = DepartmentForm(data=request.POST)
        if form.is_valid():
            new_department = form.save(commit=False)
            new_department.owner = request.user
            new_department.save()
            return redirect('departments:departments')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'departments/new_department.html', context)


@login_required
def edit_department(request, department_id):
    """Edit an existing department"""
    department = Department.objects.get(id=department_id)
    # Check to make sure the department is owned by the user
    if department.owner != request.user:
        raise Http404
    name = department.name
    university = department.university

    if request.method != 'POST':
        # initial request; pre-fill form with current entry
        form = DepartmentForm(instance=department)
    else:
        # POST data submitted, process data
        form = DepartmentForm(instance=department, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments:department', department_id=department.id)

    context = {'department': department, 'name': name, 'university': university, 'form': form}
    return render(request, 'departments/edit_department.html', context)


@login_required
def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    # Check to make sure the department is owned by the user
    if department.owner != request.user:
        raise Http404
    # BA-LETED
    Department.objects.get(id=department_id).delete()
    # After delete, redirect back to main departments page
    departments = Department.objects.filter(owner=request.user).order_by('name')
    context = {'departments': departments}
    return render(request, 'departments/departments.html', context)
