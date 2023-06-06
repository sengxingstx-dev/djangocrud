from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . models import User, Employee


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=100, required=False)
    # image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username',  'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'profile_image'
        ]


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
