from django.shortcuts import render, redirect
from .models import *

def index(request):
    projects = Project.objects.all()
    context ={
        'all_projects': projects
    }
    return render(request, 'index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


