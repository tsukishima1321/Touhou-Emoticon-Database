from django.db import models

class pictures(models.Model):
    name = models.CharField(max_length=50)
