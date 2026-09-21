from django.urls import path

from .api.views import CurrentUserView, LogoutView, RegisterView, CurrentProfileView

urlpatterns = [
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profiles/me/', CurrentProfileView.as_view(), name='current_profile'),
]