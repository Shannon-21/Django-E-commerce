from django.urls import path

from . import conversation_views

app_name = 'conversation'

urlpatterns = [
    path('', conversation_views.inbox, name='inbox'),
    path('<int:pk>/', conversation_views.detail, name='detail'),
    path('new/<int:item_pk>/', conversation_views.new_conversation, name='new'),
]
