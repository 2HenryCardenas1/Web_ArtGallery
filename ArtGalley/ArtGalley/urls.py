from django.contrib import admin
from django.urls import path
from appArtGallery.views import views_main as main_view
from appArtGallery.views import views_detail as detail
from appArtGallery.views import views_methods as methods
from appArtGallery.views import views_admin as admin_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view.pageMain, name='main'),

    path('artGalery/detalle/<int:id>', detail.detalle, name='detail'),
    path('artGallery/comprar/<int:id>', methods.getPieza, name='buy'),

    path('eliminar/<int:id>', admin_view.delete, name='delete'),
    path('eliminar-artista/<int:id>', admin_view.deleteArtista, name='deleteArtista'),
    path('eliminar-categoria/<int:id>', admin_view.deleteCategoria, name='deleteCategoria'),
    path('actualizar/<int:id>', admin_view.update, name='update'),
    path('actualizar-artista/<int:id>', admin_view.updateArtista, name='updateArtista'),

    path('artGallery/galeria', methods.allPiezas, name='gallery'),

    path('artGallery/categoria/<int:id>', methods.categorys, name='categoria'),

    path('artGallery/admin/agregarPieza', admin_view.addPieza, name='add'),
    path('artGallery/admin/agregarArtista', admin_view.addArtista, name='addArtista'),

    path('artGallery/admin/agregarCategoria', admin_view.addCategoria, name='addCategoria'),

    path('artGallery/admin/editar-elimnar', admin_view.edit_Delete, name='editarEliminar'),

    path('artGallery/admin/login', admin_view.loginUser, name='login'),
    path('artGallery/admin/logout', admin_view.logoutUser, name='logout'),

    path('searchCharacters/', methods.search, name='search')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
