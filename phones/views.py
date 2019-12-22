from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    catalog = Phone.objects.select_related().all()

    template = 'catalog.html'
    context = {'catalog': catalog}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
