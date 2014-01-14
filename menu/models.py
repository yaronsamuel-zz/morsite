from django.db import models
from orderedmodel import OrderedModel
from morsite.thumbs import ImageWithThumbsField

THUMB_W = 400
THUMB_H = 400
THUMB_SIZE = (THUMB_W , THUMB_H)

# thumb that is (19,9) is in format (w,h) gets url 19x9.jpg



class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    base_url = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.name

    def save(self, force_insert=False, force_update=False):
        """
        Re-order all items from 10 upwards, at intervals of 10.
        This makes it easy to insert new items in the middle of 
        existing items without having to manually shuffle 
        them all around.
        """
        super(Menu, self).save(force_insert, force_update)
        
        current = 10
        for item in MenuItem.objects.filter(menu=self).order_by('order'):
            item.order = current
            item.save()
            current += 10

class MenuItem(OrderedModel):
    menu = models.ForeignKey(Menu)
    link_url = models.CharField(max_length=100, help_text='URL or URI to the content, eg /about/ or http://foo.com/')
    title = models.CharField(max_length=100)
    login_required = models.BooleanField(blank=True, help_text='Should this item only be shown to authenticated users?')
    anonymous_only = models.BooleanField(blank=True, help_text='Should this item only be shown to non-logged-in users?')
    # item_picture  = ImageWithThumbsField(upload_to = 'menu/' , sizes=( (THUMB_W, THUMB_H) , ) ,magnify = False) 
    # description = models.TextField(blank=True, null=True)                                   
    
    
     
    def __unicode__(self):
        return "%s %s. %s" % (self.menu.slug, self.order, self.title)

    # @property
    # def pictureURL(self):
        # return self.item_picture.url
    
    # @property    
    # def thumb(self):
        # attr_name = 'url_%sx%s' % THUMB_SIZE
        # return getattr(self.item_picture, attr_name)