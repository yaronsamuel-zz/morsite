from django.http import HttpResponse
from django.template import RequestContext, loader

from models import ProductCategory , Product

def index(request):
    categories = ProductCategory.objects.all()

    template = loader.get_template('prices/index.html')
    context = RequestContext(request, {
        'prCategories': categories,
    })
    return HttpResponse(template.render(context))
     