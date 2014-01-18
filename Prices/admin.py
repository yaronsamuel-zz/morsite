from django.contrib import admin
from models import  Product , ProductCategory
from orderedmodel import OrderedModelAdmin

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    exclude = ('order',)
 
class CategoryAdmin(OrderedModelAdmin):
   
    search_fields = ['category_Name',
                    'category_description',
                    ]
    
    fields = ['category_Name',
              'category_description', 
              'category_image' ,
              ]
              
    list_display = ('category_Name',
              'category_description' ,
              'category_image' , 
              'reorder' , 
              )

    inlines = [ProductInline]

class ProductAdmin(OrderedModelAdmin):

           
    list_display = ('category' , 
                    'product_name',
                    'regular_price',
                    'big_price',
                    'huge_price' ,
                    'reorder'
              )
              
    search_fields = ['product_name',
                    'regular_price',
                    'big_price',
                    'huge_price']
                    
    


                
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
