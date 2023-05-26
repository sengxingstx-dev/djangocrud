from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Employee, EmployeeForm



def home(request):
    return render(request, 'base/home.html')


def employee_list(request):
    employees = Employee.objects.all()

    return render(request, 'base/emp_read.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    
    return render(request, 'base/emp_create.html', {'form': form})


def employee_search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    employees = Employee.objects.filter(
        Q(firstname__icontains=q) |
        Q(lastname__icontains=q)
    )

    context = {
        'employees': employees, 
    }
    return render(request, 'base/emp_read.html', context)


def employee_update(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(instance=employee, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(initial=employee.__dict__)
        return render(request, 'base/emp_create.html', {'form': form, 'is_update': True})


def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect('emp-read')
