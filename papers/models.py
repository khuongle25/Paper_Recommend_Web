from django.db import models
from rest_framework import serializers

# Create your models here.

class Paper(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    abstract = models.TextField()
    publication_date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.title
    
class GroupPaper(models.Model):
    group_name = models.CharField(max_length=100)
    group_description = models.TextField()
    papers = models.ManyToManyField(Paper, blank=True)
    rec_list_updated = models.BooleanField(default=True)

    def __str__(self):
        return self.group_name

class RecommendPapersList(models.Model):
    group = models.ForeignKey(GroupPaper, on_delete=models.CASCADE)
    papers = models.ManyToManyField(Paper, blank=True)
    
    def __str__(self):
        return self.group.group_name