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
    url(r'^opera/great-grand-mother-2', 'portfolio.views.ggm_2', name='great_grand_mother_2'),
    url(r'^opera/great-grand-mother', 'portfolio.views.great_grand_mother', name='great_grand_mother'),
    url(r'^opera', 'portfolio.views.opera', name='opera'),
    url(r'^film/du-fehlst', 'portfolio.views.du_fehlst', name='du_fehlst'),
    url(r'^film/soad', 'portfolio.views.soad', name='soad'),
    url(r'^film', 'portfolio.views.film', name='film'),
    url(r'^memorial/800', 'portfolio.views.eighthundret', name='800'),
    url(r'^memorial', 'portfolio.views.memorial', name='memorial'),
    url(r'^installation/reflecting-light', 'portfolio.views.reflecting_light', name='reflecting_light'),
    url(r'^installation/inside', 'portfolio.views.inside', name='inside'),
    url(r'^installation', 'portfolio.views.installation', name='installation'),
    url(r'^theatre/blindenschrift', 'portfolio.views.blindenschrift', name='blindenschrift'),
    url(r'^theatre/448', 'portfolio.views.fourfoureight', name='448'),
    url(r'^theatre', 'portfolio.views.theatre', name='theatre'),
    url(r'^dance/kylmae', 'portfolio.views.kylma', name='kylma'),
    url(r'^dance', 'portfolio.views.dance', name='dance'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)