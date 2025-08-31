from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # accounts web
    path("auth/", include("accounts.urls")),

    # todos web (home)
    path("", include("todos.urls")),
]
