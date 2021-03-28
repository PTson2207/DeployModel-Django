from django.db import models

# Create your models here.
class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    pclass = models.IntegerField(max_length=50)
    sex = models.BooleanField()
    age = models.IntegerField()
    sibsp = models.IntegerField()

    def __str__(self):
        return self.pclass
