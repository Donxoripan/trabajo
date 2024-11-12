from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    video = models.FileField(upload_to='videos/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
