from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name="Status")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "status"
        verbose_name_plural = "status"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=200, verbose_name="Autor")
    content = models.TextField(verbose_name="Sinopsis", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="libro", null=True, blank=True)
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    categories = models.CharField(max_length=200, verbose_name="Categorías", null=True, blank=True)
    status = models.CharField(max_length=200, verbose_name="Status", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        ordering = ['-created']

    def __str__(self):
        return self.title