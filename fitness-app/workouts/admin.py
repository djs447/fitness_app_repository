from django.contrib import admin
from workouts.models import Workout, WorkoutSample

class WorkoutAdmin(admin.ModelAdmin):
    pass

class WorkoutSampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Workout,WorkoutAdmin)
admin.site.register(WorkoutSample,WorkoutSampleAdmin)
