from django.db import models

class Project(models.Model):
    title= models.CharField(max_length=255)
    description= models.TextField()
    technology= models.CharField(max_length=50)
    image= models.FilePathField(path='/img')
    created_at= models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
