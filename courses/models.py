from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
import random

# generating a random rating for default
randomrating = random.choice([4.2, 4.4, 4.1, 4.2, 4.3])


class Subject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=False)

    def __str__(self):
        return self.title.upper()


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=False)
    date_created = models.DateTimeField(auto_now=True)
    overview = models.TextField(blank=True)
    coursevideo = models.CharField(max_length=2500, blank=True)
    coverImage = models.ImageField(upload_to='course_cover', blank=True)
    cost = models.CharField(default='Free', blank=True, max_length=20)
    rating = models.CharField(max_length=3, blank=True, default=randomrating)
    tags = TaggableManager()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title}  by {self.instructor}'


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=False)
    video = models.CharField(max_length=2500, blank=True)
    moduleFile = models.FileField(upload_to='Modules', blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField()

    def __str__(self):
        return f'{self.title} [{self.course}] '

    class Meta:
        ordering = ['title']
