from django.contrib import admin
from workouts.models import Workout, WorkoutSample

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'started_at', 'created', 'modified']

class WorkoutSampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Workout,WorkoutAdmin)
admin.site.register(WorkoutSample,WorkoutSampleAdmin)
