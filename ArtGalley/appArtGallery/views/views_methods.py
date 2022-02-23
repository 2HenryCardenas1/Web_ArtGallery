from django.shortcuts import render, redirect

from appArtGallery.form import Factura

from appArtGallery.models import *

from django.contrib import messages


def getPieza(request, id):
    pieza = Pieza.objects.get(id=id)
    factura = Facturacion.objects.filter(pieza_id_pieza=id)
    form = Factura(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Revisa la bandeja de entrada de tu correo para continuar con el proceso de pago.',
                         extra_tags='compra')
        return redirect('gallery')

    context = {
        'pieza': pieza,
        'form': form,
        'factura': factura
    }

    return render(request, 'forms/comprar.html', context)


def allPiezas(request):
    piezas = Pieza.objects.all().order_by('id').reverse()

    return render(request, 'options/galeria.html', {'piezas': piezas})


def search(request):
    palabra = request.GET.get('palabra', False)

    peiza_find = Pieza.objects.filter(nombre_pieza__contains=palabra)
    categoria_find = Categoria.objects.filter(nombre__contains=palabra)
    context = {
        'peiza': peiza_find,
        'categoria': categoria_find,
        'palabra': palabra
    }
    return render(request, 'options/search.html', context)


def categorys(request, id):
    categoria = Categoria.objects.get(id=id)
    piezas = Pieza.objects.select_related('categoria').filter(categoria_id=id)
    print(piezas.query)
    context = {
        'categorias': categoria,
        'piezas': piezas
    }
    return render(request, 'options/tipoarte.html', context)


def menu_list(request):
    menu_list = Categoria.objects.all()
    return {'menu': menu_list}
