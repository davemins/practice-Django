from django.contrib import admin

from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    list_filter = ('created_at', )
    search_fields = ('id', 'writer_username')
    inlines = [CommentInline]
# admin.site.register(Comment)