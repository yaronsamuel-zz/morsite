from django.contrib import admin
from menu.models import MenuItem
from orderedmodel import OrderedModelAdmin

class MenuItemAdmin(OrderedModelAdmin):
    
    list_display = (
                    'title',
                    'link_url',
                    'reorder'
          )
          
         
admin.site.register(MenuItem, MenuItemAdmin)
