from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class RegistroForm(forms.ModelForm):#Clase para el formulario de registro
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password_confirmacion = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')
    rol = forms.ChoiceField(choices=Perfil.ROLES, label='Rol')

    class Meta:#Clase Meta para definir el modelo y los campos del formulario
        model = User
        fields = ['username', 'email', 'password', 'password_confirmacion']#Campos del formulario

    #Método para validar la confirmación de la contraseña, se llama clean_<nombre_campo>
    def clean_password_confirmacion(self):#Método para validar la confirmación de la contraseña
        password = self.cleaned_data.get('password')#Obtenemos la contraseña
        password_confirmacion = self.cleaned_data.get('password_confirmacion')
        if password and password_confirmacion and password != password_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirmacion
    
class EditarPerfilForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Nueva Contraseña', required=False)
    password_confirmacion = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña', required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email']  # Los campos editables por el usuario

    # Validación para confirmar que las contraseñas coinciden
    def clean_password_confirmacion(self):
        password = self.cleaned_data.get('password')
        password_confirmacion = self.cleaned_data.get('password_confirmacion')
        if password and password_confirmacion and password != password_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirmacion

    # Lógica para actualizar la contraseña solo si el campo de contraseña no está vacío
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user