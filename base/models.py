from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    profile_image = models.ImageField(null=True, blank=True, default='profile_images/default.png', upload_to='profile_images/')

    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=6,
        choices=[('Male', 'Male'), ('Female', 'Female')],
        default='Male'
    )
    position = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
    address = models.TextField()
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=30, unique=True)
    birthday = models.DateField()
    religion = models.CharField(
        max_length=20,
        choices=[('Buddhism', 'Buddhism'), ('Christianity', 'Christianity'), ('Islam', 'Islam'), ('etc', 'etc')],
        default='Buddhism'
    )
    addition_note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='product_employee')

    def __str__(self):
        return f'{self.name}'
