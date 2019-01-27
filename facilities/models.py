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
        return self.author.__str__() + ' said ' + self.text

    def format_date(self):
        return self.created_at.strftime('%I:%M - %m-%d-%Y')


class Chemical(models.Model):
    name = models.CharField(max_length=50)
    cas = models.CharField(max_length=20)
    container_size = models.CharField(max_length=20)
    number_of_containers = models.IntegerField()
    company = models.CharField(max_length=50)
    cabinet_number = models.IntegerField()
    owner = models.CharField(max_length = 50)
    msds = models.FileField(upload_to='msds/', blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.cas