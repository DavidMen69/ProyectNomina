from django.contrib import admin
from GestionNomina.models import Departamento,Empleado,Nomina,Cargo,Rol,Usuario,Permiso
# Register your models here.

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=("nom_departamento","estado")

class CargosAdmin(admin.ModelAdmin):
    list_display=("nombre_cargo","departamento","estado")
    list_filter=("departamento",)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display=("nombres","num_documento","departamento","cargo","estado")
    search_fields=("nombres","num_documento")

admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Cargo,CargosAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Nomina)
admin.site.register(Usuario)
admin.site.register(Permiso)
admin.site.register(Rol)
