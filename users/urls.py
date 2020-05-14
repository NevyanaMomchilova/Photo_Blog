from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("sign_up/", users_views.sign_up, name="sign_up"),
    path("profile/", users_views.profile, name="profile"),

]

