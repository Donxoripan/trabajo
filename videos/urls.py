from django.urls import path
from . import views

app_name = 'videos'  # Cambiado a videos

urlpatterns = [
    path('', views.lista_videos, name='lista_videos'),  # Cambiado a lista_videos
    path('video/<int:pk>/', views.detalle_video, name='detalle_video'),  # Cambiado a detalle_video
    path('subir/', views.subir_video, name='subir_video'),  # Cambiado a subir_video
    path('video/<int:pk>/editar/', views.editar_video, name='editar_video'),  # Cambiado a editar_video
    path('video/<int:pk>/eliminar/', views.eliminar_video, name='eliminar_video'),  # Cambiado a eliminar_video
]
