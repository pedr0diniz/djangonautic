from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # automatic timestamp
    thumb = models.ImageField(default='default.png', blank=True)  # default.png manually placed in the folder, blank=True means it may be blank
    # add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body) > 50:
            return f'{self.body[:50]}...'
        else:
            return self.body
