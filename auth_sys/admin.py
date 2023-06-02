from django.contrib import admin
from .models import Users, Profile


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email', 
        'is_superuser', 
        'is_active', 
        'is_staff',
        'password',
        'time_created',
        'last_login'
        ]
    list_display_links = [
        'email'
    ]


admin.site.register(Users, UsersAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'id', 
        'fullname', 
        'birthday', 
        ]
    list_display_links = [
        'user',
        'fullname'
    ]


admin.site.register(Profile, ProfileAdmin)

