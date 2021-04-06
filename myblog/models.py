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
