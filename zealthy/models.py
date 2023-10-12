from django.db import models

# Create your models here.
class user_query(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,unique=True)
    desc=models.CharField(max_length=2000)
    status = models.CharField(max_length=50, default='new')

    def __str__(self):
        return self.name