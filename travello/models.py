from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class destination(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    
class Book(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    did=models.ForeignKey(destination, on_delete=models.CASCADE)
    fromdate=models.CharField(max_length=50)
    todate=models.CharField(max_length=50)
    nos=models.IntegerField()
    price=models.CharField(max_length=50)