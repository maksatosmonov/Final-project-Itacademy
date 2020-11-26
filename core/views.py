from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from .decorators import *
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from .utils import get_index_url



def home(request):
    return render(request, "index.html")


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class Login(LoginView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or get_index_url(self.request.user)


#     def get_redirect_url(self):
#         request = self.request
#         if request.user.is_authenticated:
#             if request.user.is_doctor:
#                 return reverse('doctor_profile', kwargs={"user_pk": request.user.pk})
#             else:
#                 return reverse('patient_profile', kwargs={"user_pk": request.user.pk})
    


class LogoutView(LogoutView):
    template_name = 'registration/logout.html'


class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_success_url(self):
        user_id = self.object.id
        return reverse_lazy('patient_form', kwargs={'user_pk': user_id})

    
class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_success_url(self):
        user_id = self.object.id
        return reverse_lazy('doctor_form', kwargs={'user_pk': user_id})


@method_decorator([login_required, doctor_required], name='dispatch')
class DoctorRegistrationView(CreateView):
    model = DoctorProfile
    form_class = DoctorForm
    template_name = 'profile/doctor_registration.html'

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get("user_pk")
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            doctor_profile = form.save(commit=False)
            user = User.objects.get(id=user_pk)
            doctor_profile.user = user
            doctor_profile.save()
            return redirect('doctor_profile', user_pk=user_pk)
        return render(request, self.template_name, {
            "form": form
        })

   
@method_decorator([login_required, patient_required], name='dispatch')
class PatientRegistartionView(CreateView):
    model = PatientProfile
    form_class = PatientForm
    template_name =  'profile/patient_registration.html'

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get("user_pk")
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            patient_profile = form.save(commit=False)
            user = User.objects.get(id=user_pk)
            patient_profile.user = user
            patient_profile.save()
            return redirect('patient_profile', user_pk=user_pk)
        return render(request, self.template_name, {
            "form": form
        })

@method_decorator([login_required, doctor_required], name='dispatch')
class DoctorUpdateView(UpdateView):
    model = DoctorProfile
    form_class = DoctorForm
    template_name = 'profile/doctor_registration.html'

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get("user_pk")
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            doctor_profile = form.save(commit=False)
            user = User.objects.get(id=user_pk)
            doctor_profile.user = user
            doctor_profile.save()
            return redirect('doctor_profile', user_pk=user_pk)
        return render(request, self.template_name, {
            "form": form
        })


def doctor_profile_detail(request, user_pk):
    try:
        doctor_profile = DoctorProfile.objects.get(user_id=user_pk)
    except DoctorProfile.DoesNotExist:
        return render(
            request, "profile/doctor_profile.html", {
                "error_message": f"Пользователь с id - {user_pk} не найден"
            }
        )
    return render(
        request, "profile/doctor_profile.html",
        {'doctor_profile': doctor_profile}
    )


def patient_profile_detail(request, user_pk):
    try:
        patient_profile = PatientProfile.objects.get(user_id=user_pk)
    except PatientProfile.DoesNotExist:
        return render(
            request, "profile/patient_profile.html", {
                "error_message": f"Пользователь с id - {user_pk} не найден"
            }
        )
    return render(
        request, "profile/patient_profile.html",
        {'patient_profile': patient_profile}
    )


def doctors(request):
    doctors = DoctorProfile.objects.all().order_by('doctor_position')
    context = {"doctors": doctors}
    return render(request, "doctors.html", context)




