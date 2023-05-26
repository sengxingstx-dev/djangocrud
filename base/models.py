from django.db import models
from django import forms



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


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'firstname': 'ຊື່',
            'lastname': 'ນາມສະກຸນ',
            'gender': 'ເພດ',
            'position': 'ຕຳແຫນ່ງ',
            'salary': 'ເງິນເດືອນ',
            'address': 'ທີ່ຢູ່',
            'email': 'ອີເມວ',
            'phone': 'ເບີໂທ',
            'birthday': 'ວັນເກີດ',
            'religion': 'ສາສະຫນາ',
            'addition_note': 'ບັນທືກເພີ່ມເຕີມ'
        }
        widgets = {
            'gender': forms.RadioSelect(),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'religion': forms.Select(),
            'address': forms.Textarea(attrs={'rows': '3'}),
            'addition_note': forms.Textarea(attrs={'rows': '3'}),
        }
