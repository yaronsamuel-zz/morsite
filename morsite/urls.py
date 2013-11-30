from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Prices/', include('Prices.urls')),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MY_STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^topmenu.html', 'menu.views.topmenu_view'),
    url(r'^weblog/sg.html', 'SliderGallery.views.slider_gallery_view'),
    url(r'^contact/', 'contact_form.contact'),
    url(r'^thanks/', 'contact_form.thanks'),
) 

