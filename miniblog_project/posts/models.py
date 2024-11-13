
from django.db import models

class Post(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('expirado', 'Expirado')
    ]

    title = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')
    expiration = models.DateField()

    def __str__(self):
        return f"Post {self.id} - {self.conteudo[:30]}"