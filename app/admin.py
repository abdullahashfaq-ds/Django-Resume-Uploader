from django.contrib import admin
from .models import ResumeModel


@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'gender', 'city', 'phone', 'email']
