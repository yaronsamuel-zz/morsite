from django.contrib import admin
from SliderGallery.models import SliderImage
from orderedmodel import OrderedModelAdmin

    
class SliderImageAdmin(OrderedModelAdmin):
    
    list_display = ('image_short_name' , 
                    'reorder'
          )
    fields = ('item_picture' , 
    
          )
          
         

admin.site.register(SliderImage, SliderImageAdmin)
