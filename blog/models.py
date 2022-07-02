from django.utils import timezone
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post (models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    content =models.TextField(max_length=10000)
    publish_date=models.DateField(default=timezone.now)
    update_date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='posts/')
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


    class Meta :
        verbose_name = "My Post"
        ordering = ['-publish_date']

