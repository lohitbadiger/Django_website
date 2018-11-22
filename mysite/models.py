from django.db import models

# Create your models here.
# database:store somethings

class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Contact(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=180)
    message=models.TextField()

    def __str__(self):
        return self.email    