from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import Forms
from webapp.models import Products
from django.core.handlers.wsgi import WSGIRequest


def products_views(request: WSGIRequest):
    products = Products.objects.all().order_by('category', 'name')
    context = {
        'products': products
    }
    return render(request, 'home.html', context=context)


def product_add(request: WSGIRequest):
    if request.method == 'GET':
        form = Forms()
        return render(request, 'product_add.html', context={'form': form})

    form = Forms(data=request.POST)
    if not form.is_valid():
        return render(request, 'product_add.html', context={'form': form})
    else:
        Products.objects.create(**form.cleaned_data)
        return redirect('home')


def product_update(request: WSGIRequest, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        form = Forms(initial={
            'name': product.name,
            'description': product.description,
            'img': product.img,
            'category': product.category,
            'remainder': product.remainder,
            'price': product.price,
            'created_at': product.created_at
        })
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = Forms(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.img = form.cleaned_data['img']
            product.category = form.cleaned_data['category']
            product.remainder = form.cleaned_data['remainder']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('home')
        else:
            return render(request, 'product_update.html', context={'from': form, 'product': product})


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {'product': product}
    return render(request, 'product_view.html', context=context)


def product_delete(request: WSGIRequest, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    if request.method == 'POST':
        product.delete()
    return redirect('home')


def out_of_stock(request: WSGIRequest):
    products = Products.objects.all().order_by('category', 'name')
    context = {
        'products': products
    }
    return render(request, 'out_of_stock.html', context=context)
