from django.contrib.auth import views as auth_views
from django.urls import path

from . import core_views
from .core_forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', core_views.index, name='index'),
    path('contact/', core_views.contact, name='contact'),
    path('signup/', core_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/core_login.html', authentication_form=LoginForm), name='login'),
    path('logout/', core_views.logout, name='logout'),
]