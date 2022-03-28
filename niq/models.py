import email
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Employee(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length = 254)
  role = models.CharField(max_length=200, default="Intern")
  department = models.CharField(max_length=200)
  reports_to = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  created_date = models.DateTimeField(default=timezone.now)
  is_manager = models.BooleanField(default=False)

  # DoB = models.DateField()

  def publish(self):
    self.created_date = timezone.now()
    self.save()

  def __str__(self):
    return self.name

