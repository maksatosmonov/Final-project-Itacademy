from django.contrib import admin
from core.models import *

admin.site.register(User)
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)

# Register your models here.
