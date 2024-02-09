from django import forms
from .models import ResumeModel
from .utils import GENDER_CHOICE, CITY_CHOICE


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICE,
        widget=forms.RadioSelect
    )
    job_city = forms.MultipleChoiceField(
        label='Prefered Job Locations',
        choices=CITY_CHOICE,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = ResumeModel
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'birth': 'Date of Birth',
            'phone': 'Mobile Number',
            'profile_img': 'Profile Image',
            'file': 'Document',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth': forms.DateInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
