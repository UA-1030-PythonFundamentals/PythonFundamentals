from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['published'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:post_detail', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:category', kwargs={'cat_id': self.id})

