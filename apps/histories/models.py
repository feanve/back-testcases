from django.db import models
from apps.projects.models import Projects

class Histories(models.Model):
    PRIORITY_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]

    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="Proyecto")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, verbose_name="Prioridad")
    criteria = models.TextField(verbose_name="Criterios de Aceptación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f'{self.name} - {self.project.name}'

    class Meta:
        verbose_name = 'Historia de Usuario'
        verbose_name_plural = 'Historias de Usuario'
        ordering = ['id']

