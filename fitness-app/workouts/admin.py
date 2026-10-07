from django.contrib import admin
from workouts.models import Comment, Workout, WorkoutSample

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'started_at', 'created', 'modified']

class WorkoutSampleAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'workout', 'content', 'created', 'modified']

admin.site.register(Workout,WorkoutAdmin)
admin.site.register(WorkoutSample,WorkoutSampleAdmin)
admin.site.register(Comment,CommentAdmin)
