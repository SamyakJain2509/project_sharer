from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    submitted = models.DateTimeField(auto_now_add=True)
    project_file = models.FileField(upload_to='project_files')
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} by {self.developer}'