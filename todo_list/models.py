from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item+' | '+str(self.completed)
    