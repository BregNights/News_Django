from django.contrib import admin
from .models import Author, Category, News, Comments

admin.site.site_header = 'ApexNews'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(Category, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'created_at')
    list_display_links = ('id', 'tittle')
    search_fields = ('id', 'tittle')

admin.site.register(News, NewsAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'created_at')
    list_display_links = ('id', 'tittle')
    search_fields = ('id', 'tittle')

admin.site.register(Comments, CommentsAdmin)
