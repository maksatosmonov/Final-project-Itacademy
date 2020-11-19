from django.db import models
from core.models import User


class Message(models.Model):
    sender = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name='sender_messages')
    receiver = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE,
        related_name='receiver_messages')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} to {}'.format(self.sender.username, self.receiver.username)