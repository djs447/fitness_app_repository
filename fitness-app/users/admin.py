from django.contrib import admin
from users.models import User, Profile

class UserAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Profile,ProfileAdmin)
