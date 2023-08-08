from django.db import models

class pictures(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=40,null=True)
    character = models.CharField(max_length=40,null=True)
    tags = models.CharField(max_length=200,null=True)
    hash_sha = models.CharField(max_length=40) #SHA-1
    likes = models.IntegerField()
