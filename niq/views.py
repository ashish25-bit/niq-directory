from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from niq.forms import EmployeeForm
import json
from .models import Employee
from datetime import date

def index(request):
  context = {
    'form': EmployeeForm(),
  }

  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    empAdded = False
    empAdded = True

    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      role = form.cleaned_data['role']
      department = form.cleaned_data['department']
      reports_to = form.cleaned_data['reports_to']
      location = form.cleaned_data['location']
      is_manager = form.cleaned_data['is_manager']

      emp = Employee(
        name=name,
        email=email,
        role=role,
        department=department,
        reports_to=reports_to,
        location=location,
        is_manager=is_manager,
        created_date=date.today()
      )

      managers = Employee.objects.filter(is_manager=True)
      if role == 'CEO':
        emp.reports_to = 'NA' 
        emp.save()
        empAdded = True

      if role == 'Intern':
        emp.is_manager = False
        emp.save()
        empAdded = True

      elif reports_to in [manager.name for manager in managers]:
        emp.save()
        empAdded = True

      if empAdded:
        return HttpResponseRedirect('display?message=Employee-Added-Successfully')
      return HttpResponseRedirect('display?message=Failed-To-Add-Employee')

  return render(request, 'index.html', context)

def delete(request):
  method =  request.GET.get('method')

  if method == 'DELETE':
    id = request.GET.get('id')

    if id == None:
      return HttpResponse("No action")

    # delete the employee
    emp = Employee.objects.get(pk=id).delete()
    return HttpResponse("Employee Deleted")

  return HttpResponse("No action")

def display(request):
  context = {
    'data': []
  }

  context['data'] = Employee.objects.all().values_list('name', 'email', 'role', 'department', 'reports_to', 'location', 'is_manager', 'pk')
  return render(request, 'display.html', context)


def custom_404_view(request, exception):
  return HttpResponse("Page not found")


def update(request, id):
  emp = Employee.objects.get(pk=id)

  # update
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    isUpdated = False

    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      role = form.cleaned_data['role']
      department = form.cleaned_data['department']
      reports_to = form.cleaned_data['reports_to']
      location = form.cleaned_data['location']
      is_manager = form.cleaned_data['is_manager']

      managers = Employee.objects.filter(is_manager=True).exclude(name=emp.name)

      emp.name = name;
      emp.email = email;
      emp.role = role;
      emp.department = department;
      emp.reports_to = reports_to;
      emp.location = location;
      emp.is_manager = is_manager;

      if role == 'CEO':
        emp.reports_to = 'NA' 
        emp.save()
        isUpdated = True

      if role == 'Intern':
        emp.is_manager = False
        emp.save()
        isUpdated = True

      elif reports_to in [manager.name for manager in managers]:
        emp.save()
        isUpdated = True

    if isUpdated:
      return HttpResponseRedirect('/display?message=Employee-Updated-Successfully')
    return HttpResponseRedirect(f'/display?message=Failed-To-Update')

  initial = {
    "name": emp.name,
    "email": emp.email,
    "role": emp.role,
    "department": emp.department,
    "reports_to": emp.reports_to,
    "location": emp.location,
    "is_manager": emp.is_manager
  }

  context = {
    "employee_data": emp,
    'form': EmployeeForm(initial=initial),
  }

  return render(request, 'update.html', context)


def custom_404_view(request, exception):
  return HttpResponse("Page not found")
