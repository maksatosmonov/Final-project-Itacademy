from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from .models import *



def chatpage(request):
    chats = Chat.objects.all()
    #     Q(message__sender=request.user) |
    #     Q(message__receiver=request.user)
    # ).distinct()
    return render(request, "chatpage.html", {"chats": chats})



def chat(request, id):
    chat_object = Chat.objects.get(id=id)
    context = {"chat": chat_object}
    return render(request, "chat.html", context)


def add_message(request):
    if request.method == 'POST':
        chat_id = request.POST.get("chat")
        chat = Chat.objects.get(id=chat_id)
        text = request.POST.get("message")
        message = Message(
            chat=chat,
            text=text,
            sender=request.user
        )
        message.save()
        return redirect(f'/chat/{ chat_id }#end')
    
    return redirect(homepage)


