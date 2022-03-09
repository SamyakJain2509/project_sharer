from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import SubmitProjectForm

def home(request):
    return render(request, 'projects/index.html', {})

@login_required
def submit_project(request):
    form = SubmitProjectForm()

    if request.method == 'POST':
        form = SubmitProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.developer = request.user
            new_project.save()
            return redirect('home')
    return render(request, 'projects/create.html', {'form': form})

@login_required
def browse(request):
    projects = Project.objects.all()

    return render(request, 'projects/browse.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    
    return render(request, 'projects/detail.html', {'project': project})