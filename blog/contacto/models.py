from django.db import models

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    mensaje = models.TextField()
    fecha_enviado= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Mensaje de: {self.email}'
