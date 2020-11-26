from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('chatpage/', chat_page, name="chat_page"),
    path('add-message/', add_message, name='add-message')
]