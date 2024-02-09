from django.shortcuts import render
from django.views import View
from .forms import ResumeForm
from .models import ResumeModel


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        return render(request, 'index.html', {'form': form})
