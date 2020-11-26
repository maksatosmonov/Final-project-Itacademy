from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from .models import *
from core.models import DoctorProfile


def chat_page(request):
    messages = Message.objects.all()
    return render(request, "chat.html", {"messages": messages})


def add_message(request):
    if request.method == 'POST':
        user = request.user
        text = request.POST.get("message")
        Message.objects.create(
            owner=user,
            text=text
        )
        return redirect("chat_page")
    return redirect("chat_page")
