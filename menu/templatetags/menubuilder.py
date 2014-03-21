from menu.models import MenuItem
from django import template
from django.core.cache import cache

MENU_WIDTH = 870
WIDE_WIDTH = 130

register = template.Library()

def build_menu(parser, token):
    """
    builds menu from {% load_menu %}
    """
    return MyMenuObject()

    
class MyMenuObject(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        
       
        request = context.get('request' , None)
        if request:
            current_path = request.path
            user = context['request'].user
        else:
            #some random string
            current_path = '@@@@$@@@@$@@@@%@@@@@&@@'
            user = None
            
        menuItems = MenuItem.objects.all()
        
        context['highighted'] = None
        isHompage = context.get('homepage' , False)
        
        if isHompage:
             current_path = 'index.html'
        
        
        for item in menuItems:          
            if item.link_url.endswith(current_path):
                context['highlighted'] = item
                break
        
            #checks if it is a post
            if 'weblog' in current_path and \
                'weblog' in item.link_url:
                    
                    context['highlighted'] = item
                    break
        
        

        context['menuitems'] =  getMenuItemsTupples(menuItems)
        
        return ''
    
    
def getMenuItemsTupples(menuItems):
    
    retList = []
    count = 0
    for item in menuItems:
        if len(item.title) > 10:
            count += 1
    
    totalWidth  = MENU_WIDTH - count * WIDE_WIDTH
    menu_item_width = (totalWidth* 1.0 ) / (len(menuItems) - count)
    
    for item in menuItems:
        if len(item.title) > 10:
            width = WIDE_WIDTH
        else:
            width = menu_item_width
        
        retList.append( (item , width) )
    
    return retList
    
    

register.tag('load_menu', build_menu)

