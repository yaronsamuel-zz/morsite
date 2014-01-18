from django.http import HttpResponse
from django.template import RequestContext, loader

from models import ProductCategory , Product

def index(request):
    categories = ProductCategory.objects.all()
    
    tripples = []
    for i in xrange( 0 ,len(categories) , 3):
        tripples.append(categories[i:i+3])
    
    template = loader.get_template('prices/prices.html')
    context = RequestContext(request, {
        'product_categories': tripples,
    })
    
    return HttpResponse(template.render(context))
     