from django.db import models
from django.contrib.auth.models import AbstractUser

from PIL import Image
# Create your models here.

class Employee(models.Model):
    full_name    = models.CharField(max_length=200)
    email        = models.CharField(max_length=100)
    contact      = models.CharField(max_length=100)
    address      = models.TextField()
    picture      = models.ImageField(upload_to='uploads/', max_length=255, null=True, blank=True)

    username     = models.CharField(max_length=100, unique=True)
    password     = models.CharField(max_length=100, default=1)

    def __str__(self):
        return self.full_name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    class Meta:
        db_table = 'employee'

class Shift(models.Model):
    name         = models.CharField(max_length=100)
    start_time   = models.TimeField(default=None)
    end_time     = models.TimeField(default=None)
    status       = models.BooleanField(default=True)
    date         = models.DateField(default=None)

    employee     = models.ForeignKey(Employee, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shift'