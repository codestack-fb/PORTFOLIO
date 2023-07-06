from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(default='default.png')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    link = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name