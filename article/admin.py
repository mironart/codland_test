from django.contrib import admin
from .models import Article

class ArtecleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'date_created', ]
admin.site.register(Article, ArtecleAdmin)