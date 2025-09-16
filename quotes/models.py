from django.db import models

# Create your models here.
class Quote(models.Model):
    text = models.TextField(max_length=260, unique=True)
    author = models.CharField(max_length=50)
    tag = models.CharField(max_length=20, db_index=True)
    year = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
