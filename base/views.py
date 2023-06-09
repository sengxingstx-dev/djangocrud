from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Employee, Product

from .models import User
from .forms import EmployeeForm, SignUpForm, UserProfileForm, ProductForm



def home(request):
    return render(request, 'base/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/register.html', {'form': form})


def profile(request, pk):
    return render(request, 'registration/profile.html')


def update_profile(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)
        form = UserProfileForm(request.POST ,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=pk)
    else:
        user = User.objects.get(id=pk)
        form = UserProfileForm(initial=user.__dict__)
    return render(request, 'registration/update_profile.html', {'form': form})


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


def product_list(request):
    products = Product.objects.all()

    return render(request, 'base/prod_read.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    
    return render(request, 'base/prod_create.html', {'form': form})


def product_update(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        product = Product.objects.get(id=id)
        form = ProductForm(initial=product.__dict__)

    return render(request, 'base/prod_create.html', {'form': form, 'is_update': True})


def product_delete(request, id):
    prodcut = Product.objects.get(id=id)
    prodcut.delete()

    return redirect('prod-read')


def product_search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(
        Q(name__icontains=q)
    )

    context = {
        'products': products, 
    }
    return render(request, 'base/prod_read.html', context)