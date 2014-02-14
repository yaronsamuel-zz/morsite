from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','morsite.views.homepage' , name='index'),
    url(r'^500.shtml','morsite.views.Page500' , name='error500'),
    url(r'^index.html','morsite.views.homepage'),
    url(r'^kisses.html','morsite.views.kissesPage'),
    url(r'^course.html','morsite.views.coursePage'),
    
   (r'^grappelli/', include('grappelli.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Prices/', include('Prices.urls')),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MY_STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^topmenu.html', 'menu.views.topmenu_view'),
    url(r'^hompageGallery.html', 'Gallery.views.homepage_gallery_view'),
    url(r'^Gallery.html', 'Gallery.views.gallery_view'),
    url(r'^contact/', 'contact_form.views.contact'),
    url(r'^thanks/', 'contact_form.views.thanks'),
    url(r'^contact/sidebar', 'contact_form.views.contact'),    
    (r'^tinymce/', include('tinymce.urls')),
) 

