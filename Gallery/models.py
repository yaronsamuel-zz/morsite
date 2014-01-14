from django.db import models
from orderedmodel import OrderedModel
from morsite.thumbs import ImageWithThumbsField
import os

THUMB_H_FLOAT = 200.0
THUMB_HEIGHT = int(THUMB_H_FLOAT)
THUMB_WIDTH = 200


# thumb that is (19,9) is in format (w,h) gets url 19x9.jpg

class GalleryImage(OrderedModel):
    
    picture_width = models.IntegerField(blank=True, null=True,)
    picture_height = models.IntegerField(blank=True, null=True,)
    item_picture  = ImageWithThumbsField(upload_to = 'SliderGallery/' , magnify = False) 
    homepage = models.BooleanField(default = False)
    gallery = models.BooleanField(default = True)
    title = models.CharField(max_length=30 , blank=True)
    description = models.CharField(max_length=50 , blank=True)
    
    def save(self):
        """
        Re-order all items from 10 upwards, at intervals of 10.
        This makes it easy to insert new items in the middle of 
        existing items without having to manually shuffle 
        them all around.
        """
        
        self.picture_height = THUMB_HEIGHT
        # self.picture_width  = 1.0 * self.item_picture.width * (THUMB_H_FLOAT / self.item_picture.height )
        # self.picture_width = int(self.picture_width)
        self.picture_width = THUMB_WIDTH
        
        
        self.item_picture.sizes = ( (self.picture_width, self.picture_height) , ) 
        super(GalleryImage, self).save()
        
    def __unicode__(self):
        return u'%s' % (os.path.basename(self.item_picture.name) , )
       
    def image_short_name(self):
        return self.__unicode__()
        
    image_short_name.short_description = 'Name'
   
    @property
    def pictureURL(self):
        return self.item_picture.url
    
    @property    
    def thumb_size(self):
        return (self.picture_width , self.picture_height)
    
    @property    
    def thumb(self):
        
        (w,h) = self.thumb_size
        split = self.pictureURL.rsplit('.',1)
        thumb_url = '%s.%sx%s.%s' % (split[0],w,h,split[1])
        
        return thumb_url