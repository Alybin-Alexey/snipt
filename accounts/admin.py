from django.contrib import admin

from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_pro',)
    search_fields = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
