from django.contrib import admin

from snipts.models import Comment, Snipt

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    allow_add = False

class SniptAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'tags', 'user', 'lexer', 'public', 'created', 'modified',)
    search_fields = ('title', 'user__username', 'tags', 'lexer', 'id',)
    ordering = ('created',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

admin.site.register(Snipt, SniptAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'snipt', 'created', 'modified',)
    search_fields = ('comment', 'user__username',)
    ordering = ('created',)

admin.site.register(Comment, CommentAdmin)
