from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("password-change/", views.change_password, name="password_change"),

    # reset
    path("password-reset/", views.password_reset_request, name="password_reset_request"),
    path("reset-confirm/<uidb64>/<token>/", views.password_reset_confirm, name="password_reset_confirm"),
]
