from django.contrib import admin
from .models import Category, Post # llama estas clases para permitir trabajar con ellas las mismas pertenecen a model del blog 

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display = ('title','autor','published','post_categories')
    ordering=('autor','published')
    # en caso de ordenar por un solo elemento hay que dejarle una coma 
    search_fields=('title','content','autor__username','categories__name')
    # cuando se va a buscar por autor se debe colocar el nombre de la variable creada con username y antes doble piso, no se puede buscar 
    # por solo autor ya que la base de datos esta repacionada con categoria y da error 
    # el caso de la categoria es igual que el de autor 
    date_hierarchy='published'
    # hace un filtro en el administrador para clasificacion por fechas 
    list_filter= ('autor__username','categories__name')

    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")]) 
        
    post_categories.short_description = 'Categorías' 

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)