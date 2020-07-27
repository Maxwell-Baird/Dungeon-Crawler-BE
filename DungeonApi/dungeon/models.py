from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField

class Npc(models.Model):
    name = models.CharField(max_length=70, blank=False, default='Loneliness')
    attack = models.PositiveIntegerField(blank=False, default=5)
    defense = models.PositiveIntegerField(blank=False, default=5)
    health = models.PositiveIntegerField(blank=False, default=10)
    dialogue = ArrayField(JSONField())
    options = ArrayField(JSONField())
    location = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=256, blank=False, default='Its a thing')
