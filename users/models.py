from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    net_id = models.CharField(max_length=9, default='', blank=True)
    phone_number = models.CharField(max_length=20, default='', blank=True)
    institution = models.CharField(max_length=80, default='', blank=True)
    cost_center = models.IntegerField(default=0, blank=True)
    cost_center_end_date = models.DateField(max_length=30, blank=True, null=True)
    supervisor = models.CharField(max_length=50, default='', blank=True)
    activation_form = models.FileField(upload_to='activation_forms/', blank=True, null=True)
    training_form = models.FileField(upload_to='training_forms/', blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
