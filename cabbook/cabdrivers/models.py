from django.db import models

# Create your models here.

class driver_signup_db(models.Model):
    Name = models.CharField(max_length=100)
    Email_Address = models.EmailField(max_length=100)
    Mobile_Number=models.CharField(max_length=10)
    City_Drive = (
        ('Ten', 'Tenkasi'),
        ('Kdnl', 'Kadayanallur'),
        ('Tvl', 'Tirunelveli')
    )
    City = models.CharField(max_length=10, choices=City_Drive)
    Vehicle_Type = (
        ('cr', 'Car'),
        ('bk', 'Bike'),
        ('Au', 'Auto')
    )
    Vehicle = models.CharField(max_length=6, choices=Vehicle_Type)
    Vehicle_Number = models.CharField(max_length=10)
    Bank_Account = models.BigIntegerField()
    Profile_Picture = models.ImageField(upload_to='cabdrivers/profile')
    License_Number = models.CharField(max_length=20)
    Aadhaar_Card = models.CharField(max_length=12)
    RC_Photo = models.ImageField(upload_to='cabdrivers/RC')
    Vehicle_Insurance = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name 


