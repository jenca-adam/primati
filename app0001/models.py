from django.db import models

class Prispevok(models.Model):
    obsah=models.CharField(max_length=1000)
    published=models.DateTimeField(auto_now_add=True)
# Create your models here.
