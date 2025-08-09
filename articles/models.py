from django.db import models
from datetime import datetime


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=True)
    published_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
