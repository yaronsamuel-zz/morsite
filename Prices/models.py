from django.db import models
from morsite.thumbs import ImageWithThumbsField
from orderedmodel import OrderedModel

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

    
    @property
    def pictureURL(self):
        if self.product_picture:
            return  self.product_picture.url        
        else:
            return None
        
        
      
    @property
    def thumb125(self):
        return self.product_picture.url_125x125
        
    @property    
    def thumb200(self):
        return self.product_picture.url_200x200
        

    
    def __unicode__(self):
        return u'%s' % (self.product_name, )
    
    
 
    

    