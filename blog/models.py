from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст посту")
    published_date = models.DateTimeField(auto_now=True)
