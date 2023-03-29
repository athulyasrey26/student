from django.conf import settings
from django.conf.urls.static import static

from .views import *
from django.urls import path
# app_name='studentapp'

urlpatterns = [

    path('',home,name='home'),
    path('login/', login_view, name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('buttonpage/', buttonpage, name='buttonpage'),
    path('application_view/', application_view, name='application_view'),
    path('load_courses', load_courses, name='load_courses'),
    path('logout', user_logout, name='logout'),
    path('application-submit', applicationsubmit, name = "applicationsubmit"),


]

