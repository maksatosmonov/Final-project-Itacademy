from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import *


class DoctorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        return user


class PatientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
        ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        return user


class DoctorForm(ModelForm):
    class Meta:
        model = DoctorProfile
        fields = [
            "passport_id",
            "date_of_birth",
            "gender",
            "photo",     
            "phone_number",
            "adress",
            "licences_number",
            "date_of_work",
            "hospital_name",
            "doctor_position",
        ]

class PatientForm(ModelForm):
    class Meta:
        model = PatientProfile
        fields = [
            "passport_id",
            "date_of_birth",
            "gender",
            "photo",     
            "phone_number",
            "adress",
            "weight",
            "height",
            "allergic_person",
            "blood_type",
            "heart_disease",
        ]

