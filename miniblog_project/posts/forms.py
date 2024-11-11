
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'status', 'expiration']
        widgets = {
            'expiration': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }