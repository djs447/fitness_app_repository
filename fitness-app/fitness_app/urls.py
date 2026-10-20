
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from workouts.api.views import CommentViewSet, WorkoutViewSet, WorkoutSampleViewSet
from users.api.views import GoalViewSet, ProfileViewSet, RegisterView

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'workout_samples', WorkoutSampleViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/login/', obtain_auth_token, name='login'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/', include(router.urls)),
]

urlpatterns += [
    path('api/users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
