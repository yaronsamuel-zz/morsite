from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
# from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Prices/', include('Prices.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.STATIC_ROOT}),
) 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns.extend()