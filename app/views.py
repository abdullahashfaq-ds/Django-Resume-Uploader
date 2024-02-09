from django.shortcuts import render
from django.views import View
from .forms import ResumeForm
from .models import ResumeModel


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = ResumeModel.objects.all()
        return render(request, 'index.html', {'form': form, 'candidates': candidates})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = ResumeForm()
        return render(request, 'index.html', {'form': form})
