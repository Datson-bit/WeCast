from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title +'|'+ str(self.author)

    def get_absolute_url(self):
        return reverse('article-details', args=(str(self.id)))



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, default=1 )
    name = models.CharField(max_length=255, default=2)
    comment = models.TextField(default=1)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


class Sport(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null= True)
    img = models.ImageField(null=True, blank=True, upload_to="images/")                                                                   

    def __str__(self):
        return self.title +'|'+ str(self.author)
