#from turtle import title
#from unittest.util import _MAX_LENGTH
from django.db import models
from uuid import uuid4

# Create your models here.

class Books(models.Model):
  id_post = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  realease_year = models.IntegerFiled()
  state = models.ImageField(max_length=50)
  pages = models.IntegerField()
  pulblishing_company = models.CharField(max_length=255)
  create_at = models.DateField(auto_now_add=True)