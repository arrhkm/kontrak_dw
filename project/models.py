from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name
