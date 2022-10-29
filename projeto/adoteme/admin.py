from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Usuario, Estado, Unidade, Animal, ListaAdocao


admin.site.register(Usuario, auth_admin.UserAdmin)
admin.site.register(Estado)
admin.site.register(Unidade)
admin.site.register(Animal)
admin.site.register(ListaAdocao)
