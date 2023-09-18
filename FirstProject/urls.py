from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include, re_path
from . import settings
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    re_path(r'^$', RedirectView.as_view(pattern_name='accounts:home', permanent=True)),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)