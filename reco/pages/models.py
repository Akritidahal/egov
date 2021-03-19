from django.db import models
from django.contrib.auth.models import User
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

# Create your models heure.
class Citizen(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    dob=models.DateField()
    phone=models.CharField(max_length=10)
    age=models.IntegerField(default=16)
    gender=models.IntegerField(choices=GENDER_CHOICES)
    father_name=models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50,blank=True)
    husband_name=models.CharField(max_length=50,blank=True)
    grandfather_name=models.CharField(max_length=50)
    father_citizen_number=models.CharField(max_length=12,blank=True)
    husband_citizenship_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    mother_citizen_number = models.CharField(max_length=12, blank=True)
    husband_citizen_number = models.CharField(max_length=12, blank=True)
    birth_certificate_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    applicant_photo= models.ImageField(upload_to='photos/%Y/%m/%d/')
    father_citizenship_photo=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    mother_citizenship_photo=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_verified=models.BooleanField(default=False)

    def __str__(self):
        return self.user

