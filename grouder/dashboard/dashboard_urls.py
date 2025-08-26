from django.urls import path

from . import dashboard_views

app_name = 'dashboard'

urlpatterns = [ 
    path('', dashboard_views.index, name='index'),
]