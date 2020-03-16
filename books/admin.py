from django.contrib import admin
from .models import Book, Category, Status

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class StatusAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author')
    ordering = ('author', 'user')
    search_fields = ('title','content')
    list_filter = ('title', 'author')

    def book_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    book_categories.short_description = "Categorías"
    
    def book_status(self, obj):
        return ", ".join([c.name for c in obj.status.all().order_by("name")])
    book_status.short_description = "Status"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Book, BookAdmin)