from Gallery.models import GalleryImage , HOMEPAGE_THUMB_WIDTH  , HOMEPAGE_THUMB_HEIGHT
from django import template


INTERVAL = 3000

register = template.Library()

    
    
def build_gallery(parser, token):
    """
    {% gallery gallery_name %}
    """
    try:
        tag_name, gallery_name = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    return GalleryObject(gallery_name)

class GalleryObject(template.Node):
    def __init__(self, gallery_name):
        self.gallery_name = gallery_name

    def render(self, context):
        images = GalleryImage.objects.filter(homepage = True)
        urls = [image.thumb_hompage for image in images]
        imagesItemsArray = []
        
        for i in xrange(4):
            
            offset = (len(urls) / 4 ) * i
            imagesArr = urls[offset : ] + urls [: offset]
            interval = INTERVAL * i
            imagesItemsArray.append((imagesArr , interval))
        
        
        current_path = context['request'].path
        user = context['request'].user
        context['imagesItemsArray'] = imagesItemsArray
        context['width'] = HOMEPAGE_THUMB_WIDTH
        context['height'] = HOMEPAGE_THUMB_HEIGHT
        
        return ''
    

  
    
register.tag('gallery', build_gallery)

