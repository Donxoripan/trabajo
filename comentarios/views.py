from django.shortcuts import render, get_object_or_404, redirect
from .models import Comentario
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm

# Vista para listar los comentarios
def lista_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'comentarios/lista_comentarios.html', {'comentarios': comentarios})

# Vista para ver un comentario específico
def ver_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    return render(request, 'comentarios/ver_comentario.html', {'comentario': comentario})

# Vista para editar un comentario
@login_required
def editar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    
    # Solo los usuarios con rol 'editor' o 'administrador' pueden editar
    if not (request.user.perfil.rol == 'editor' or request.user.perfil.rol == 'administrador'):
        return redirect('comentarios:lista_comentarios')

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('comentarios:ver_comentario', id=comentario.id)
    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'comentarios/editar_comentario.html', {'form': form, 'comentario': comentario})

# Vista para eliminar un comentario
@login_required
def eliminar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    
    # Solo los usuarios con rol 'editor' o 'administrador' pueden eliminar
    if not (request.user.perfil.rol == 'editor' or request.user.perfil.rol == 'administrador'):
        return redirect('comentarios:lista_comentarios')

    if request.method == 'POST':
        comentario.delete()
        return redirect('comentarios:lista_comentarios')

    return render(request, 'comentarios/eliminar_comentario.html', {'comentario': comentario})

@login_required
def subir_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user  # Asociamos el comentario al usuario actual
            comentario.save()
            return redirect('comentarios:lista_comentarios')  # Redirigimos a la lista de comentarios
    else:
        form = ComentarioForm()

    return render(request, 'comentarios/subir_comentario.html', {'form': form})