from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Video  # Cambiado a Video
from .forms import VideoForm  # Cambiado a VideoForm
from django.contrib.auth.decorators import login_required

def lista_videos(request):
    videos = Video.objects.all().order_by('-fecha_subida')  # Cambiado a Video
    return render(request, 'videos/lista_videos.html', {'videos': videos})  # Cambiado a lista_videos

def detalle_video(request, pk):
    # Obtener el video específico por su pk
    video = get_object_or_404(Video, pk=pk)
    
    # Obtener todos los videos (o ajustar esto según lo que necesites)
    videos_list = Video.objects.all()

    # Pasar tanto el video como la lista de videos al template
    return render(request, 'videos/detalle_video.html', {'video': video, 'videos_list': videos_list})

@login_required
def subir_video(request):  # Cambiado a subir_video
    if request.user.perfil.rol in ['editor', 'administrador']:
        if request.method == 'POST':
            form = VideoForm(request.POST, request.FILES)  # Cambiado a VideoForm
            if form.is_valid():
                video = form.save(commit=False)
                video.autor = request.user
                video.save()
                messages.success(request, 'Video subido exitosamente.')  # Mensaje de éxito
                return redirect('videos:detalle_video', pk=video.pk)  # Cambiado a detalle_video
        else:
            form = VideoForm()
        return render(request, 'videos/subir_video.html', {'form': form})  # Cambiado a subir_video
    else:
        return redirect('videos:lista_videos')  # Cambiado a lista_videos

@login_required
def editar_video(request, pk):  # Cambiado a editar_video
    video = get_object_or_404(Video, pk=pk)
    if request.user == video.autor or request.user.perfil.rol == 'administrador':
        if request.method == 'POST':
            form = VideoForm(request.POST, request.FILES, instance=video)  # Cambiado a VideoForm
            if form.is_valid():
                form.save()
                messages.success(request, 'Video actualizado exitosamente.')  # Mensaje de éxito
                return redirect('videos:detalle_video', pk=video.pk)  # Cambiado a detalle_video
        else:
            form = VideoForm(instance=video)
        return render(request, 'videos/editar_video.html', {'form': form, 'video': video})  # Cambiado a editar_video
    else:
        messages.error(request, 'No tienes permiso para editar este video.')  # Mensaje de error
        return redirect('videos:detalle_video', pk=pk)  # Cambiado a detalle_video

@login_required
def eliminar_video(request, pk):  # Cambiado a eliminar_video
    video = get_object_or_404(Video, pk=pk)
    if request.user == video.autor or request.user.perfil.rol == 'administrador':
        if request.method == 'POST':
            video.delete()
            messages.success(request, 'Video eliminado exitosamente.')  # Mensaje de éxito
            return redirect('videos:lista_videos')  # Cambiado a lista_videos
        else:
            return render(request, 'videos/eliminar_video.html', {'video': video})  # Cambiado a eliminar_video
    else:
        messages.error(request, 'No tienes permiso para eliminar este video.')  # Mensaje de error
        return redirect('videos:detalle_video', pk=pk)  # Cambiado a detalle_video
