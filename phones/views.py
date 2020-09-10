from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort_catalog = request.GET

    template = 'catalog.html'

    all_phone = Phone.objects.all()
    if 'sort-name' in sort_catalog:
        all_phone = Phone.objects.order_by('name')
    if 'min-price' in sort_catalog:
        all_phone = Phone.objects.order_by('price')
    if 'max-price' in sort_catalog:
        all_phone = Phone.objects.order_by('-price')

    context = {'phones': all_phone,}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    all_phone = Phone.objects.all()
    for phone in all_phone:
        if phone.slug.lower() == slug:
            context = {'phones': phone, }
            return render(request, template, context)




