from django.http import HttpResponse
from django.template import RequestContext, loader

from models import SliderImage , THUMB_H

def slider_gallery_view(request):
    
    images = SliderImage.objects.all()
    template = loader.get_template('SliderGallery/index.html')
    context = RequestContext(request, {
        'images': images,
        'picture_height' : THUMB_H,
    })
    return HttpResponse(template.render(context))
     
