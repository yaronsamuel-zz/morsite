from django.db import models
from morsite.thumbs import ImageWithThumbsField
from orderedmodel import OrderedModel

class ProductCategory(OrderedModel):
    category_Name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=100  , blank=True)
    category_image =  models.ImageField(upload_to='products/categories')
    
    def __unicode__(self):
        return u'%s' % (self.category_Name, )
    
    @property
    def pictureURL(self):
        if self.category_image:
            return  self.category_image.url        
        else:
            return None

class Product(OrderedModel):
    
    category = models.ForeignKey(ProductCategory)
    product_name = models.CharField(max_length=50)    
    # product_description = models.CharField(max_length=500  , blank=True)    
    product_picture = ImageWithThumbsField(upload_to='products/',
                                    sizes=() , null=True ,blank=True)    

    regular_price = models.IntegerField()
    big_price = models.IntegerField(default = 0 , null=True)
    huge_price = models.IntegerField(default = 0 , null=True)    

    
    @property
    def pictureURL(self):
        if self.product_picture:
            return  self.product_picture.url        
        else:
            return None
        
    @property
    def priceStr(self):
        prices = [ self.regular_price , self.big_price ,self.huge_price]
        prices = [str(p) for p in prices if p > 0]
        return ' / '.join(prices)

        

    
    def __unicode__(self):
        return u'%s' % (self.product_name, )
    
    
 
    

    