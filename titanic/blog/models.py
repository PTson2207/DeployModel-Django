from django.db import models

# Create your models here.
class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pclass = models.IntegerField(max_length=50)
    sex = models.BooleanField()
    age = models.IntegerField()
    sibsp = models.IntegerField()
