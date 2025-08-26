from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.core_urls')),
    path('items/', include('item.item_urls')),
    path('dashboard/', include('dashboard.dashboard_urls')),
    path('inbox/', include('conversation.conversation_urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
