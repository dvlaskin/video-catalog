from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<int:category_id>', views.catalog, name='catalog'),
    path('video/<int:video_id>', views.video_link, name='video'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
