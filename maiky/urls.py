from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import settings

urlpatterns = patterns('',
    url(r'^$', 'portfolio.views.home', name='home'),
    url(r'^news/schnitzlersdreams', 'portfolio.views.home', name='schnitzlerdreams'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)