from django import forms
from .models import Employee, Login 

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
        widgets = {
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
        }
