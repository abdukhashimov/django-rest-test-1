from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        if len(str(self.title)) > 20:
            return self.title[:20]
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        if len(str(self.title)) > 20:
            return self.title[:20] + '...'
        return self.title
