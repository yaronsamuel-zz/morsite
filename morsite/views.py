from django.http import HttpResponse
from django.template import RequestContext, loader
from zinnia.models.entry import Entry

FEATURED_NUMBER = 3

def homepage(request):
    
    template = loader.get_template('zinnia/my_entry_list.html')
    context = RequestContext(request, {
        'object_list': Entry.published.filter(featured=True)[:FEATURED_NUMBER],
        'homepage' : True , 
    })
    return HttpResponse(template.render(context))
     