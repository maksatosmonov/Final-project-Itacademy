from django.db import models
from core.models import User


class Chat(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    users = models.OneToOneField(
        to=User, 
        on_delete=models.CASCADE, 
        blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(
        to=Chat, 
        on_delete=models.SET_NULL,
        null=True,
        related_name="message" 
    )
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    sender = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="sent_messages")
        
    receiver = models.ForeignKey(
        to=User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="received_messages")

    class Meta:
        ordering = ["date"]