from django.http import HttpResponse
from django.template import RequestContext, loader

from models import GalleryImage

# IMEAGES_IN_ROW = 6
# ROW_HEIGHT = 129
# PADDING = 35 * 2
# MIN_IFRAME_HEIGHT = 500

def homepage_gallery_view(request):
    
    images = GalleryImage.objects.filter(homepage = True)
    
    template = loader.get_template('gallery/hompageGallery.html')
    context = RequestContext(request, {
       
    })
    return HttpResponse(template.render(context))
     
def gallery_view(request):
    
    images = GalleryImage.objects.filter(gallery = True)
    
    template = loader.get_template('gallery/gallery.html')    
    context = RequestContext(request, {
        'images': images,
    })
    return HttpResponse(template.render(context))
    