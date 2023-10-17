from django.urls import path
from . import views
from .views import DepartamentoListView,detalleDepartamento, edicionDepartamento, crearDepartamento,editarDepartamento,eliminarDepartamento
from .views import listar_cargos,CargoUpdateView,CargoDeleteView
from .views import listar_empleados,EmpleadoCreateView,EmpleadoUpdateView,EmpleadoDeleteView
urlpatterns = [
    path('', views.BASE,name='BASE' ),
    # --------------------model Departamento ---------------------------------
    path('departamentos/', DepartamentoListView.as_view(),name='departamento_list'),
    path('crearDepartamento/', views.crearDepartamento),
    path('detalleDepartamento/detalle/<int:pk>/', views.detalleDepartamento, name='detalleDepartamento'),
    path('edicionDepartamento/edicion/<int:pk>/', views.edicionDepartamento, name='edicionDepartamento'),
    path('editarDepartamento/editar/<int:pk>/', views.editarDepartamento, name='editarDepartamento'),
    path('departamentos/eliminar/<int:pk>/', views.eliminarDepartamento, name='eliminarDepartamento'),
    # ------------------Inicio Del Model Cargo--------------------------------
    path('cargo', views.listar_cargos, name='listar_cargos'),
    path('departamento/', views.get_departamento, name='get_departamento'),
    path('crearCargo/', views.crearCargo, name='crearCargo'),
    path('cargos/editar/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/eliminar/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),

    # ------------------Inicio Del Model Departamento--------------------------------
    path('empleado', views.listar_empleados, name='listar_empleados'),
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
]
