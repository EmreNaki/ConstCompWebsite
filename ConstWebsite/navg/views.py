from django.shortcuts import render
from .models import PastProject, FutureProject
from .forms import MessageForm
from django.http import HttpResponse
from django.contrib import messages


def home(response):
    return render(response, "navg/home.html", {})

def history(request):
    return render(request, 'navg/history.html')

def pprojects(request):
        PProjects= PastProject.objects.all()
        context = {'PProjects': PProjects,}
        return render(request, 'navg/projects.html', context)


def fprojects(request):
    FProjects = FutureProject.objects.all()
    context = {'FProjects': FProjects,}
    return render(request, 'navg/fprojects.html', context)

def reachus(request):
    form_class = MessageForm
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'MESAJINIZ ALINMIŞTIR')
    else:
        form = MessageForm()
    return render(request, 'navg/reachus.html', {'form': form})