
from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('subir/', views.subir_comentario, name='subir_comentario'),  # Ruta para agregar comentarios
    path('lista/', views.lista_comentarios, name='lista_comentarios'),  # Ruta para ver lista de comentarios
    path('ver/<int:id>/', views.ver_comentario, name='ver_comentario'),
    path('editar/<int:id>/', views.editar_comentario, name='editar_comentario'),
    path('eliminar/<int:id>/', views.eliminar_comentario, name='eliminar_comentario'),
]
