from django.shortcuts import render, redirect

from appArtGallery.models import *


# Create your views here.
def detalle(request, id):
    join = Pieza.objects.select_related('artista').filter(id=id)
    print(join.query)

    context = {
        'list': join,

    }
    return render(request, 'options/detalle.html', context)
