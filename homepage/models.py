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
    
class Post(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return 1
