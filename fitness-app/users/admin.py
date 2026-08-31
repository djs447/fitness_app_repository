from django.contrib import admin
from users.models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','full_name')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name')

admin.site.register(User, UserAdmin)
admin.site.register(Profile,ProfileAdmin)
