from django.urls import path

from . import views

from .views import *

app_name = 'home_services'

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    # path("profile/", views.IndexView.as_view(), name="profile"),
    # path('add_location/', location_view, name='add_location'),
    path("cform/", cform, name='customer_form'),
    path("pform/", pform, name='provider_form'),
    # path("<int:pk>", views.DetailView.as_view(), name="detail"),
    path('submit/', form_submit, name='profile_submit'),
    path('customer/', customer_submit, name='customer_submit'),
    # path('contact/', contact_form_view, name='contact_form'),
    # path('puser/', profile_submit, name='puser_submit'),
]