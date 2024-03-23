from django.urls import reverse

from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name





class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DR', 'Draft'
        Published = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    publish_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)


    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish_time']
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("detail_link", args=[self.slug])











