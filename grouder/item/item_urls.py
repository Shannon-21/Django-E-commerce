from django.urls import path

from . import item_views

app_name = 'item'

urlpatterns = [
    path('', item_views.items, name='items'),
    path('new/', item_views.new, name='new'),
    path('<int:pk>/', item_views.detail, name='detail'),
    path('<int:pk>/edit/', item_views.edit, name='edit'),
    path('<int:pk>/delete/', item_views.delete, name='delete'),
] 