from django.contrib import admin
from users.models import Goal, User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','full_name')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name')

class GoalAdmin(admin.ModelAdmin):
    list_display = ('profile', 'description')

admin.site.register(User, UserAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Goal,GoalAdmin)
