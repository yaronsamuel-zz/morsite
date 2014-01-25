from django.db import models
from orderedmodel import OrderedModel
from morsite.thumbs import ImageWithThumbsField
import os

HOMEPAGE_THUMB_SIZE = (100*2,100*2)
HOMEPAGE_THUMB_WIDTH = 170
HOMEPAGE_THUMB_HEIGHT = 170
GALLERY_THUMB_SIZE = (123 * 2 , 112*2) 
SIZES = [HOMEPAGE_THUMB_SIZE , GALLERY_THUMB_SIZE]

# thumb that is (19,9) is in format (w,h) gets url 19x9.jpg

class GalleryImage(OrderedModel):
    
    item_picture  = ImageWithThumbsField(upload_to = 'Gallery/' , magnify = False , sizes = SIZES) 
    homepage = models.BooleanField(default = False)
    gallery = models.BooleanField(default = True)
    title = models.CharField(max_length=30 , blank=True)
    description = models.CharField(max_length=50 , blank=True)
    
    # def save(self , ):
        # """
        # Re-order all items from 10 upwards, at intervals of 10.
        # This makes it easy to insert new items in the middle of 
        # existing items without having to manually shuffle 
        # them all around.
        # """
       
        # # sizes = []
        # # if self.homepage:
            # # sizes.append(HOMEPAGE_THUMB_SIZE)
            
        # # if self.gallery:    
            # # sizes.append(GALLERY_THUMB_SIZE)
                
        # # if sizes:
            # # self.item_picture.sizes = sizes
        
        # super(GalleryImage, self).save()
        
        
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
        
        (w,h) = HOMEPAGE_THUMB_SIZE
        split = self.pictureURL.rsplit('.',1)
        thumb_url = '%s.%sx%s.%s' % (split[0],w,h,split[1])
        
        return thumb_url
        
    @property    
    def thumb_gallery(self):
        
        (w,h) = GALLERY_THUMB_SIZE
        split = self.pictureURL.rsplit('.',1)
        thumb_url = '%s.%sx%s.%s' % (split[0],w,h,split[1])
        
        return thumb_url
        
        