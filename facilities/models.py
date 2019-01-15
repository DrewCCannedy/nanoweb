from django.db import models
from users.models import CustomUser


class Message(models.Model):
    text = models.CharField(max_length=150)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    message_choices = (
        ('L', 'low'),
        ('M', 'medium'),
        ('H', 'high'),
    )
    importance = models.CharField(max_length=1, choices=message_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.__str__() + ' ' + self.created_at.__str__()
