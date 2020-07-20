from django.db import models

from django.db import models


class Encounter(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    image = models.CharField(max_length=200, default='')
    
