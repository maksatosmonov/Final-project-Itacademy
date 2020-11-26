from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('chatpage/', chatpage, name="chatpage"),
    path('chat/<int:id>/', chat, name="chat"),
    path('add-message/', add_message, name='add-message')
]