from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .others import *
from  embed_video.admin  import AdminVideoMixin, EmbedVideoField


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_varified = models.BooleanField(default = False)
    token = models.CharField(max_length=255)

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogModel, self).save(*args, **kwargs)


class CoursePartModel(models.Model):
    title = models.CharField(max_length=100)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    video = EmbedVideoField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(CoursePartModel, self).save(*args, **kwargs)


class ServiceModel(models.Model):
    title = models.CharField(max_length=100)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ServiceModel, self).save(*args, **kwargs)


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Recent(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.title