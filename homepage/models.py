from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.email}'
    
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', height_field=None, width_field=None)

    def __str__(self):
        return self.title