
from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone
from datetime import timedelta

class Post(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('expirado', 'Expirado')
    ]

    id = models.AutoField(primary_key=True)

    title = models.CharField(
        max_length=127,
        validators=[MinLengthValidator(5)],
        blank=False,
        null=True)

    date = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    max_image = {
        'size': 50,
        'width': 256,
        'height': 256,
    }

    def clean(self):
        if len(self.content) > 255:
            raise ValidationError(
                'A imagem não pode exceder 255 caracteres.')

        # Bloqueia imagens maiores que max_image['size']
        if self.image and self.image.size > self.max_image['size'] * 1024 * 1024:
            raise ValidationError(f'A imagem não pode exceder {
                self.max_image['size']} MB.')
        
    def save(self, *args, **kwargs):

        # Redimensionar a imagem antes de salvar
        if self.image:
            img = Image.open(self.image)

            if img.height > self.max_image['height'] or img.width > self.max_image['width']:
                output_size = (
                    self.max_image['height'],
                    self.max_image['width']
                    )
                img.thumbnail(output_size)

        # Salvar a imagem redimensionada em memória
        img_io = io.BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)

        # Substituir a imagem original pela redimensionada
        self.image = InMemoryUploadedFile (
            img_io,
            'ImageField',
            self.image.name,
            'image/png',
            img_io.getbuffer().nbytes,
            None
        )

        self.full_clean()
        super().save(*args, **kwargs)


    content = models.TextField(
        validators=[MinLengthValidator(10), MaxLengthValidator(255)],
        blank=False
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ativo')

    expiration = models.DateField(default=lambda: (timezone.now().date() + timedelta(days=365)))

    def __str__(self):
        return f"Post {self.id} - {self.conteudo[:30]}"