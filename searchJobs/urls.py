from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static


urlpatterns = [
    path('', include('website.urls')),
    path('core/', include('core.urls')),
    path('contas/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

