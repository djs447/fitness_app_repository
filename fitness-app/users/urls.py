from django.urls import path

from .api.views import (
    CurrentProfileView,
    CurrentUserView,
    LogoutView,
    RegisterView,
    ShareableUsersView,
    UpdateProfilePictureView,
)

urlpatterns = [
    path("me/", CurrentUserView.as_view(), name="current_user"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profiles/me/", CurrentProfileView.as_view(), name="current_profile"),
    path(
        "profiles/me/update_picture/",
        UpdateProfilePictureView.as_view(),
        name="update_profile_picture",
    ),
    path(
        "<int:user_id>/shareable/", ShareableUsersView.as_view(), name="shareable_users"
    ),
]
