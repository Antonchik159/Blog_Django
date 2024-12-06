from django.db import models
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ім'я автора")
    bio = models.TextField(verbose_name="Біо")
    def __str__(self) -> str:
        return f"{self.name}, {self.bio}"

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст посту")
    published_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='media/', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def published_recently(self):
        return now() - self.published_date <= timedelta(days=7)


    def __str__(self) -> str:
        return f"{self.title}, {self.content}, {self.author}, {self.published_date}"
