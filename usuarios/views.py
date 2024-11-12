from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistroForm, EditarPerfilForm
from .models import Perfil
from django.http import Http404

# Vista para el registro de usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # No guardamos aún para asignar la contraseña
            user.set_password(form.cleaned_data['password'])  # Encriptamos la contraseña con el método set_password
            user.save()  # Guardamos el usuario

            # Asignamos el rol al perfil
            user.perfil.rol = form.cleaned_data['rol']
            user.perfil.save()

            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('usuarios:login')
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})

# Vista para el inicio de sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)  # Autenticamos al usuario

        if usuario is not None:
            login(request, usuario)  # Iniciamos sesión
            return redirect('usuarios:perfil')  # Redirigimos al perfil del usuario

        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')

# Vista para el cierre de sesión
@login_required
def logout_view(request):
    logout(request)  # Cerramos la sesión
    return redirect('usuarios:login')  # Redirigimos al login

# Vista para ver el perfil de usuario
@login_required
def perfil(request):
    # Obtener el perfil del usuario actual
    perfil = request.user.perfil  # Suponiendo que cada usuario tiene un perfil asociado
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})

# Vista para editar el perfil de usuario
@login_required
def editar_perfil(request):
    user = request.user  # El usuario autenticado

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Guardamos los cambios en el usuario (username, email, y password si se cambió)

            # Cerrar sesión después de guardar los cambios
            logout(request)

            messages.success(request, 'Perfil actualizado con éxito. Por favor, inicia sesión nuevamente.')

            # Redirigir al login después de cerrar la sesión
            return redirect('usuarios:login')

    else:
        form = EditarPerfilForm(instance=user)

    return render(request, 'usuarios/editar_perfil.html', {'form': form})

@login_required
def eliminar_usuario(request, user_id):
    # Verifica si el usuario que está solicitando la eliminación es el mismo que el que quiere eliminar
    if not request.user.is_superuser and request.user.id != user_id:
        messages.error(request, 'No tienes permiso para eliminar este perfil.')
        return redirect('usuarios:perfil')  # Redirige si no tiene permisos

    # Obtener al usuario que queremos eliminar
    usuario_a_eliminar = get_object_or_404(User, id=user_id)

    # Si la solicitud es un POST, proceder a eliminar el usuario
    if request.method == 'POST':
        # Eliminar el usuario
        usuario_a_eliminar.delete()

        # Cerrar sesión del usuario actual
        logout(request)

        # Mensaje de éxito
        messages.success(request, 'Tu cuenta ha sido eliminada con éxito.')

        # Redirigir al login después de la eliminación
        return redirect('usuarios:login')  # Redirigir al login después de la eliminación

    # Si no es un POST, se muestra la página de confirmación
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario_a_eliminar})

@login_required
def lista_usuarios(request):
    # Obtener todos los usuarios registrados
    usuarios = User.objects.all()  # O si deseas filtrarlo por algo específico, usa .filter()
    
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})