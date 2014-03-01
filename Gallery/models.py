from django.db import models
from orderedmodel import OrderedModel
from morsite.thumbs import ImageWithThumbsField
import os

HOMEPAGE_THUMB_SIZE = (170,170)
HOMEPAGE_THUMB_WIDTH = 170
HOMEPAGE_THUMB_HEIGHT = 170
GALLERY_THUMB_SIZE = (123 * 2 , 112*2) 
SIZES = [GALLERY_THUMB_SIZE , ]

# thumb that is (19,9) is in format (w,h) gets url 19x9.jpg

class GalleryImage(OrderedModel):
    
    item_picture  = ImageWithThumbsField(upload_to = 'Gallery/' , magnify = False , sizes = SIZES) 
    homepage = models.BooleanField(default = False)
    gallery = models.BooleanField(default = True , help_text='Decides whether the picture is shown in the gallery.')
    title = models.CharField(max_length=30 , blank=True)
    description = models.CharField(max_length=50 , blank=True)
      
        
    def __unicode__(self):
        return u'%s' % (os.path.basename(self.item_picture.name) , )
       
    
    def Title(self):
        if not self.title:
            return "Untitled"
        return self.title
    
    Title.short_description = 'Title'
    
    def image_short_name(self):
        return self.__unicode__()
        
    image_short_name.short_description = 'Name'
   
    @property
    def pictureURL(self):
        return self.item_picture.url
    

    @property    
    def thumb_hompage(self):
        return self.thumb_gallery
        
        # (w,h) = HOMEPAGE_THUMB_SIZE
        # split = self.pictureURL.rsplit('.',1)
        # thumb_url = '%s.%sx%s.%s' % (split[0],w,h,split[1])
        
        # return thumb_url
        
    @property    
    def thumb_gallery(self):
        (w,h) = GALLERY_THUMB_SIZE
        split = self.pictureURL.rsplit('.',1)
        thumb_url = '%s.%sx%s.%s' % (split[0],w,h,split[1])
        
        return thumb_url
        
        