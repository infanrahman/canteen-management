from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Category, Employee, Login,Order,Hod

admin.site.register(Login)
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Hod)