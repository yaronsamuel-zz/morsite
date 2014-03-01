from menu.models import MenuItem
from django import template
from django.core.cache import cache

MENU_WIDTH = 870
MAX_PICUTE_HEIGHT = 150

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
        context['menuitems'] = menuItems

        menu_item_width = (MENU_WIDTH* 1.0 ) / len(menuItems)
        context['menu_item_width'] = menu_item_width
        
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

            
        return ''
    
    
    

register.tag('load_menu', build_menu)

