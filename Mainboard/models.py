from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    liked = models.TextField()# Исправить на список лайкнувших
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

class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datecreation = models.DateTimeField(auto_now_add=True)


