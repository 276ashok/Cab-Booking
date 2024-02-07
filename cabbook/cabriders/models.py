from django.db import models

# Create your models here.

class cabriders_signup(models.Model):
    Name = models.CharField(max_length = 100)
    Phone_Number = models.BigIntegerField()
    Email = models.EmailField(max_length = 100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    DoB = models.DateField()
    Emergency_Contact = models.BigIntegerField()
    Password = models.CharField(max_length = 20)

    def __str__(self):
        return self.Name