from __future__ import unicode_literals
from django.contrib import auth
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    image_url1 = models.CharField(max_length=1000,blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def getsummary(self):
        len_string = len(self.text)
        summary_string = self.text[:len_string/2]+'....'
        return summary_string