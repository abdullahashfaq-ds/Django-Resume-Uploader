from django import forms
from .models import ResumeModel


class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = '__all__'
