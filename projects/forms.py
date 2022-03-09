from django import forms
from .models import Project

class SubmitProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'project_file', 'description', 'image')