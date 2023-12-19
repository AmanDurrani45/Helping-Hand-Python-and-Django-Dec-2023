from django.urls import path

app_name="user_profile"

from . import views

from .views import *

urlpatterns = [
    # path('index', index, name='index'),
    # path('submit/', form_submit, name='profile_submit'),
    # path('c/', customer_submit, name='customer_submit'),
    # path('user_profile/', user_profile, name='user_profile'),
    path('profile/', user_profile, name='user_profile'),
    path('edit_profile/<str:username>/', edit_profile, name='edit_profile'),
    path("signup/", views.sign_up, name="sign_up"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("create_profile/<int:id>/", views.create_profile, name="create_profile"),
]
