from django.db import models
from django.utils import timezone

class Category(models.Model):
    """
        Model for Category Name
    """

    name = models.CharField('CATEGORY', max_length=255)
    created_at = models.DateTimeField('CreateDate', default=timezone.now)

    def __str__(self):
        return self.name



class Post(models.Model):
    """
        Model for displaying blog articles.
    """

    title = models.CharField('title', max_length=255)
    text = models.TextField('Content')
    created_at = models.DateTimeField('CreateDate', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='CATEGORY', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
        Add Comments Field
    """

    name = models.CharField('Name : ', max_length=30, default='Anon')
    text = models.TextField('Content')
    post = models.ForeignKey(Post, verbose_name='Article Name', on_delete=models.PROTECT)
    created_at = models.DateField('Create DateTime', default=timezone.now)

    def __str__(self):
        return self.text[:10]