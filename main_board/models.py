from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    datecreation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    CATEGORY_CHOICES = (
        ('TK', 'Танки'),
        ('HL', 'Хилы'),
        ('DD', 'ДД'),
        ('BY', 'Торговцы'),
        ('GM', 'Гилдмастеры'),
        ('QG', 'Квестгиверы'),
        ('BS', 'Кузнецы'),
        ('SK', 'Кожевники'),
        ('PM', 'Зельевары'),
        ('SM', 'Мастера заклинаний'),
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='HL')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('main')

class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datecreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'


