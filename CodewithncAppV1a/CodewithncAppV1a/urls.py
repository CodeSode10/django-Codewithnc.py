from django.contrib import admin
from django.urls import path, include
from .views import *
from os import stat
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import *

urlpatterns = [
    path('', include('Home.urls')),

    path('api/', include('Home.urls_api')),

    path('froala_editor/',include('froala_editor.urls')),

    path('admin@dj2001/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()