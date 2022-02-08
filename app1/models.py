from django.db import models

class Memes(models.Model):
    id=models.IntegerField(primary_key=True,blank=True)
    name=models.TextField(max_length=200)
    url=models.TextField(max_length=200)
    width=models.IntegerField(blank=True)
    height=models.IntegerField(blank=True)
    box_count=models.IntegerField(blank=True)
    def __str__(self):
        return self.name

# Create your models here.
