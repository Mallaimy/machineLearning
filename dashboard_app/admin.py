from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'age', 'nombre_de_personnes', 'predictions')

admin.site.register(Data, DataAdmin)
