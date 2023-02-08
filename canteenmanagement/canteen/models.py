from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Employee(models.Model):
    username= models.CharField(max_length=40)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department=models.CharField(max_length=200,null=True, blank=True)
    division=models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.username



class Hod(models.Model):
    username= models.CharField(max_length=40)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name


class Order(models.Model):
    guest_name=models.CharField(max_length=200,null=True, blank=True)
    category_name= models.CharField(max_length=40)
    user_id = models.CharField(max_length=50)
    guest = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    servingtype=models.CharField(max_length=200,null=True, blank=True)
    date=models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.category_name



