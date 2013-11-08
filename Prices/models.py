from django.db import models
from morsite.thumbs import ImageWithThumbsField
from orderedmodel import OrderedModel
from morsite.settings import MEDIA_URL
import os

class ProductCategory(OrderedModel):
    category_Name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=100  , blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.category_Name, )

class Product(OrderedModel):
    category = models.ForeignKey(ProductCategory)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=500  , blank=True)
    comments = models.CharField(max_length=300 , blank=True)
    product_picture = ImageWithThumbsField(upload_to='products/',
                                    sizes=((125,125),(200,200)) , null=True ,blank=True)    

    regular_price = models.IntegerField()
    big_price = models.IntegerField(default = 0 , null=True)
    huge_price = models.IntegerField(default = 0 , null=True)
    datePublished = models.DateTimeField('date published')
    
    
    def generateThumbnailPath(self , size , size2 = None):
        if size2 is None:
            size2 = size
            
        path , ext = os.path.splitext(self.pictureURL)
        newExt = "%sx%s%s" % (size , size2 , ext)
        return "%s.%s" % (path , newExt) 
    
    @property
    def pictureURL(self):
        return "%s%s" % (
                    MEDIA_URL ,
                    self.product_picture.name)        
        
        
      
    @property
    def thumb125(self):
        return self.generateThumbnailPath(125)
        
    @property    
    def thumb200(self):
        return self.generateThumbnailPath(200)
        

    
    def __unicode__(self):
        return u'%s' % (self.product_name, )
    
    
 
    

    