import random
from django.shortcuts import render

from appArtGallery.models import *


def pageMain(request):
    list = Pieza.objects.all()
    join = Pieza.objects.select_related('artista')
    dic = []
    dic2 = []
    categoria = Categoria.objects.all()
    for l in list:
        dic.append(l)

    for l2 in list:
        dic2.append(l2)

    select = random.sample(dic, 3)
    select2 = random.sample(dic2, 3)

    return render(request, 'index.html', {'list': select, 'list2': select2, 'category': categoria})


