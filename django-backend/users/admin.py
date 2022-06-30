from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from users.models import PostSend


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    exclude = ['last_name', 'first_name', ]
    list_display = ['email', 'username', ]


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PostSend, PostAdmin)
