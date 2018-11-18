from django.contrib import admin
from .models import Cliente, Bicicleta, Arriendo

admin.site.register(Cliente)
admin.site.register(Bicicleta)
admin.site.register(Arriendo)