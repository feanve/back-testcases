from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.TextField(verbose_name="Name")
    status = models.BooleanField(verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f'{self.name} - {self.status}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['id']