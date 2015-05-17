from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import settings

urlpatterns = patterns('',
    url(r'^$', 'portfolio.views.home', name='home'),
    url(r'^news', 'portfolio.views.news', name='news'),
    url(r'^about', 'portfolio.views.about', name='about'),
    url(r'^impressum', 'portfolio.views.impressum', name='impressum'),
    url(r'^works', 'portfolio.views.works', name='works'),
    url(r'^opera/street-opera-stockholm', 'portfolio.views.street_opera', name='street_opera'),
    url(r'^opera', 'portfolio.views.opera', name='opera'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)