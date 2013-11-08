from django.contrib import admin
from models import  Product , ProductCategory
from orderedmodel import OrderedModelAdmin

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    exclude = ('order',)
 
class CategoryAdmin(OrderedModelAdmin):
    # fieldsets = [
        # (None,               {'fields': ['category_Name']}),
        # ('Description',      {'fields': ['category_description'],
                              # 'classes': ['collapse']})
                              # ]
    
    search_fields = ['category_Name',
                    'category_description',
                    ]
    
    fields = ['category_Name',
              'category_description', 
              ]
              
    list_display = ('category_Name',
              'category_description' ,
              'reorder' , 
              )
              
    # list_filter = ['datePublished']

    inlines = [ProductInline]

class ProductAdmin(OrderedModelAdmin):

           
    list_display = ('category' , 
                    'product_name',
                    'product_description' ,
                    'comments' , 
                    'regular_price',
                    'big_price',
                    'huge_price' ,
                    'reorder'
              )
              
    search_fields = ['product_name',
                    'product_description',
                    'comments' , 
                    'regular_price',
                    'big_price',
                    'huge_price']
                    
    list_filter = ['datePublished']
    


                
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
