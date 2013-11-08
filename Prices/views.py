from django.http import HttpResponse
from django.template import RequestContext, loader

from models import ProductCategory , Product
from morsite.settings import STATIC_URL

def index(request):
    categories = ProductCategory.objects.all()

    template = loader.get_template('prices/index.html')
    context = RequestContext(request, {
        'prCategories': categories,
        'STATIC_URL' : STATIC_URL
    })
    return HttpResponse(template.render(context))
     