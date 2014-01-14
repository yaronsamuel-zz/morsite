from django.contrib import admin
from menu.models import Menu, MenuItem
from orderedmodel import OrderedModelAdmin

class MenuItemInline(admin.TabularInline):
    model = MenuItem

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline,]

    
class MenuItemAdmin(OrderedModelAdmin):
    
    list_display = ('menu' , 
                    'title',
                    'link_url',
                    # 'description',
                    'login_required' ,
                    'anonymous_only' , 
                    # 'item_picture',
                    'reorder'
          )
          
         
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
