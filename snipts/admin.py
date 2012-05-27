from django.contrib import admin

from snipts.models import Favorite, Snipt


class SniptAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    list_display = ('title', 'slug', 'user', 'lexer', 'public', 'blog_post', 'created', 'modified', 'publish_date',)
    search_fields = ('title', 'user__username', 'lexer', 'id', 'key',)
    ordering = ('-created',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Snipt, SniptAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    readonly_fields = ('snipt', 'user',)
    list_display = ('snipt', 'user', 'created',)
    search_fields = ('snipt', 'user',)
    ordering = ('-created',)

admin.site.register(Favorite, FavoriteAdmin)
