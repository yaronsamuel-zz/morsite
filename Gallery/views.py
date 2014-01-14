from django.http import HttpResponse
from django.template import RequestContext, loader

from models import GalleryImage , THUMB_HEIGHT

IMEAGES_IN_ROW = 6
ROW_HEIGHT = 129
PADDING = 35 * 2
MIN_IFRAME_HEIGHT = 500

def slider_gallery_view(request):
    
    images = GalleryImage.objects.filter(homepage = True)
    template = loader.get_template('SliderGallery/index.html')
    context = RequestContext(request, {
        'images': images,
        'picture_height' : THUMB_HEIGHT,
    })
    return HttpResponse(template.render(context))
     
def gallery_view(request):
    
    imagesCount = len(GalleryImage.objects.filter(gallery = True))
    iframe_height = ( (imagesCount) / IMEAGES_IN_ROW) * ROW_HEIGHT
    
    # add if their is modulo
    if imagesCount % IMEAGES_IN_ROW != 0:
        iframe_height += ROW_HEIGHT 
    iframe_height += PADDING
    
    iframe_height = max([iframe_height , MIN_IFRAME_HEIGHT])
    
    template = loader.get_template('Gallery/Gallery.html')    
    context = RequestContext(request, {
        'iframe_height' : iframe_height,
    })
    return HttpResponse(template.render(context))
    
    
def Iframe_gallery_view(request):
    
    images = GalleryImage.objects.filter(gallery = True)
    template = loader.get_template('Gallery/IframeGallery.html')    
    context = RequestContext(request, {
        'images': images,
        # 'picture_height' : THUMB_HEIGHT,
    })
    return HttpResponse(template.render(context))