"""ehospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/doctor/', views.DoctorSignUpView.as_view(), name='doctor_signup'),
    path('signup/patient/', views.PatientSignUpView.as_view(), name='patient_signup'),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('appointment/', views.appointment, name="appointment"),
    path('doctor_form/<int:user_pk>/', views.DoctorRegistrationView.as_view(), name="doctor_form"),
    path('patient_form/<int:user_pk>/', views.PatientRegistartionView.as_view(), name="patient_form"),
    path('doctor_profile/<int:user_pk>/', views.doctor_profile_detail, name="doctor_profile"),
    path('patient_profile/<int:user_pk>/', views.patient_profile_detail, name="patient_profile"),
    path('doctors/', views.doctors, name="doctors"),


]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)