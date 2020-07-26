from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.TextField(max_length=100)
  pub_date = models.DateTimeField()
  content = models.TextField(max_length=500)
  
  def __str__(self):
    return self.title