from django.contrib import admin
from .models import ResumeModel


@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'gender', 'city', 'phone',
        'email', 'profile_img', 'file'
    ]
