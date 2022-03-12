from django.db import models
from account.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    DISPLAY_POST_CHOICES = (
        ('everyone', 'Everyone'),
        ('friends', 'Friends'),
    )
    
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='post/imges/', default='blog/images/blog-img.jpg/')
    description = models.CharField(max_length=255, blank=True)
    display_post = models.CharField(max_length=10, choices=DISPLAY_POST_CHOICES, default='everyone')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
	# tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})