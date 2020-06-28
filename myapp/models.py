from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)
    image = models.ImageField(upload_to='leaderpics', blank=True)

    def __str__(self):
        return self.name


class PythonCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:post_list_by_slug', args = [self.slug])

class Python(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    text = models.TextField()
    category = models.ForeignKey(PythonCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    created_by =models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='python-img', blank=True)
    link = models.URLField(blank=True)
    class Meta:
        ordering = ('-publish_date',)
        index_together = (('id', 'slug'), )


    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myapp:python_detail', args = [self.id, self.slug])


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:portfolio_list_by_category', args = [self.slug])

class Portfolio(models.Model):
    category = models.ForeignKey(PortfolioCategory, null=True, blank=True, on_delete=models.CASCADE )
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='portfolio-img', blank=True)
    link = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Django(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ('-publish_date',)
        index_together = (('id', 'slug'), )

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

class JavaScript(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ('-publish_date',)
        index_together = (('id', 'slug'), )

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

class React(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ('-publish_date',)
        index_together = (('id', 'slug'), )

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
