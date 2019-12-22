from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort:
        catalog = Phone.objects.select_related().all().order_by(sort)
    else:
        catalog = Phone.objects.select_related().all()
    template = 'catalog.html'
    context = {'catalog': catalog}
    return render(request, template, context)


def show_product(request, slug):
    data = Phone.objects.select_related().get(slug=slug)
    template = 'product.html'
    context = {'data': data}
    return render(request, template, context)
