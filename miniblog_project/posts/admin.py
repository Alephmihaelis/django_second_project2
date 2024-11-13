from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'image', 'title', 'content', 'expiration', 'status')
    search_fields = ('title', 'content')
    list_filter = ('status', 'date', 'expiration')
