
from django.db import models

class Post(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('expirado', 'Expirado')
    ]

    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')
    expiration = models.DateTimeField()

    def __str__(self):
        return f"Post {self.id} - {self.conteudo[:30]}"