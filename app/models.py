from django.db import models
from .utils import STATE_CHOICE


class ResumeModel(models.Model):
    title = models.CharField(max_length=100)
    birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    pin_code = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='images', blank=True)
    file = models.FileField(upload_to='files', blank=True)
