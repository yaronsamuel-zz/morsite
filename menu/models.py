from django.db import models
from orderedmodel import OrderedModel

class MenuItem(OrderedModel):

    link_url = models.CharField(max_length=100, help_text='URL or URI to the content, eg /about/ or http://foo.com/')
    title = models.CharField(max_length=100)                             

    def __unicode__(self):
        return "%s %s. %s" % (self.menu.slug, self.order, self.title)
