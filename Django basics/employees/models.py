from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images', default='images/default.png')
    designation = models.CharField(max_length=100)
    emailAddress = models.EmailField(max_length=100, unique=True)
    phoneNumber = models.CharField(max_length=12, blank=True, unique=True)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        return f" {self.lastName} {self.firstName.title()}"
