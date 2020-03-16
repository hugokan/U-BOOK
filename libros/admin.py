from django.contrib import admin
from .models import Libro

# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'image', 'categories', 'status', 'created', 'updated')
    

admin.site.register(Libro, LibroAdmin)