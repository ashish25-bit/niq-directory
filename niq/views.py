from django.shortcuts import render
from django.http import HttpResponse
from niq.forms import EmployeeForm
import json
from .models import Employee
from datetime import date

def index(request):
  context = {
    'form': EmployeeForm(),
    'message': "",
    'data': []
  }

  if request.method == 'POST':
    form = EmployeeForm(request.POST)

    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      role = form.cleaned_data['role']
      department = form.cleaned_data['department']
      reports_to = form.cleaned_data['reports_to']
      location = form.cleaned_data['location']
      is_manager = form.cleaned_data['is_manager']

      managers = Employee.objects.filter(is_manager=True)
      if reports_to in [manager.name for manager in managers]:
        emp = Employee.objects.create(
          name=name,
          email=email,
          role=role,
          department=department,
          reports_to=reports_to,
          location=location,
          is_manager=is_manager,
          created_date=date.today()
        )
        context["message"] = "Employee added successfully"

      else:
        context["message"] = "Manager not present"

  data = Employee.objects.all()
  context["data"] = data
  return render(request, 'index.html', context)

def sample(request):
  data = {
    "name": request.GET.get('name'),
    "prev": int(request.GET.get('prev')),
    "next": int(request.GET.get('next')),
    "data": [
      "data",
      "data2"
    ]
  }
  data = json.dumps(data)
  return HttpResponse(data)

def custom_404_view(request, exception):
  return HttpResponse("Page not found")
