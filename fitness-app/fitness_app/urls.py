
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from workouts.api.views import WorkoutViewSet, WorkoutSampleViewSet
from users.api.views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'workout_samples', WorkoutSampleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/login/', obtain_auth_token, name='login'),
    path('api/', include(router.urls)),
]

urlpatterns += [
    path('api/users/', include('users.urls')),
]
