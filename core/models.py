from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="Doctor",
        primary_key=True,
        )

    passport_id = models.CharField(max_length=14, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'))
    gender = models.CharField(max_length=255, choices=gender, default='MALE')
    photo = models.ImageField(upload_to='staticfiles/mediafiles/', null=True, blank=True)
    phone_number = models.CharField(max_length=10)
    adress = models.TextField(blank=True, null=True)
    licences_number = models.CharField(max_length=20, unique=True)
    date_of_work = models.DateTimeField()
    hospital_name = models.CharField(max_length=255)
    doctor_position = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class PatientProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="Patient",
        primary_key=True,
        )
    passport_id = models.CharField(max_length=14, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = (
        ('m', 'MALE'),
        ('f', 'FEMALE'))
    gender = models.CharField(max_length=255, choices=gender, default='MALE')
    photo = models.ImageField(upload_to ='staticfiles/mediafiles/', null=True, blank=True)
    phone_number = models.CharField(max_length=10)
    adress = models.TextField(blank=True, null=True)

    weight = models.IntegerField()
    height = models.IntegerField()
    allergic_person = (
        ('yes', 'yes, I have'),
        ('non', 'no, I do not have'))
    allergic_person = models.CharField(max_length=255, choices=allergic_person, default='no, I do not have')
    blood_type = (
        ('A',  'Blood_type=A'),
        ('B',  'Blood_type=B'),
        ('O',  'Blood_type=O'),
        ('AB', 'Blood_type=AB'))
    blood_type = models.CharField(max_length=20, choices=blood_type, default='Blood_type=A')
    heart_disease = (
        ('Yes', 'Yes, I have heart_disease'),
        ('No', 'No, I do not have have heart_disease'))
    heart_disease = models.CharField(max_length=20, choices=heart_disease, default='No, I do not have have heart_disease')

    def __str__(self):
        return self.user.username

