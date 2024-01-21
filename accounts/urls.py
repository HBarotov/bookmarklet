from django.urls import path

from .views import dashboard, edit, register, user_detail, user_follow, user_list

urlpatterns = [
    path("edit/", edit, name="edit"),
    path("register/", register, name="register"),
    path("users/", user_list, name="user_list"),
    path("users/follow/", user_follow, name="user_follow"),
    path("users/<username>/", user_detail, name="user_detail"),
    path("", dashboard, name="dashboard"),
]
