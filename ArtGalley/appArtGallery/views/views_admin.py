from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render,get_object_or_404

from appArtGallery.models import *
from appArtGallery.form import AddPieza, ArtistaForm, CategoriaForm
from appArtGallery.form import Update
from appArtGallery.form import UpdateArtista
from django.contrib import messages


def loginUser(request):
    if request.method == 'POST':

        _usr = request.POST['user']
        _password = request.POST['pwd']

        user = authenticate(request, username=_usr, password=_password)

        print(user)
        if user:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'options/login.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'options/login.html', {'user': loginUser})

@login_required
def logoutUser(request):
    logout(request)
    return redirect('main')


@login_required
def addPieza(request):
    form = AddPieza(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pieza agregada correctamente !!', extra_tags='guardar')
        return redirect('gallery')
    context = {
        'form': form
    }
    return render(request, 'forms/agregar.html', context)



@login_required
def addArtista(request):
    form = ArtistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Artista agregado correctamente !!', extra_tags='guardarArtista')
        return redirect('editarEliminar')
    context = {
        'form': form
    }
    return render(request, 'forms/agregar-artista.html', context)

@login_required
def addCategoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Categoria agregada correctamente !!', extra_tags='guardarCategoria')
        return redirect('main')

    context = {
        'form': form
    }
    return render(request, 'forms/agregar-categoria.html', context)
@login_required
def edit_Delete(request):
    pieza = Pieza.objects.all()
    artista = Artista.objects.all()
    categoria = Categoria.objects.all()
    context ={
        'piezas' : pieza,
        'artistas' : artista,
        'categorias' : categoria
    }
    return render(request,'forms/editar-eliminar.html',context)


@login_required
def delete(request, id):
    pieza_delete = get_object_or_404(Pieza, id=id)
    pieza_delete.delete()
    messages.success(request, 'La pieza de arte se elimino correctamente', extra_tags='delete')
    return redirect('gallery')


@login_required
def deleteArtista(request, id):
    artista_delete = get_object_or_404(Artista, id=id)
    artista_delete.delete()
    messages.success(request, 'El artista  se elimino correctamente', extra_tags='deleteArtista')
    return redirect('editarEliminar')


@login_required
def deleteCategoria(request, id):
    categoria_delete = get_object_or_404(Categoria, id=id)
    categoria_delete.delete()
    messages.success(request, 'La categoria se elimino correctamente', extra_tags='deleteCategoria')
    return redirect('editarEliminar')


@login_required
def update(request, id):
    pieza_update = Pieza.objects.get(id=id)
    form = Update(request.POST or None,request.FILES, instance=pieza_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'La peiza se ha actualizado con exito!!', extra_tags='update')
        return redirect('detail', pieza_update.id)

    context = {
        'pieza_update': pieza_update,
        'form': form
    }

    return render(request, 'forms/update-pieza.html', context)


@login_required
def updateArtista(request, id):
    artista_update = Artista.objects.get(id=id)
    form = UpdateArtista(request.POST or None, instance=artista_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'El artista se ha actualizado con exito!!', extra_tags='updateArtista')
        return redirect('editarEliminar')

    context = {
        'artista_update': artista_update,
        'form': form
    }

    return render(request, 'forms/update-artista.html', context)