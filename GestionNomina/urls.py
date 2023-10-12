from django.urls import path
from . import views
from .views import DepartamentoListView, DepartamentoCreateView,DepartamentoUpdateView,DepartamentoDeleteView
from .views import listar_cargos, CargoCreateView,CargoUpdateView,CargoDeleteView
from .views import listar_empleados,EmpleadoCreateView,EmpleadoUpdateView,EmpleadoDeleteView
urlpatterns = [
    path('', views.BASE,name='BASE' ),
    # --------------------model Departamento ---------------------------------
    path('departamentos/', DepartamentoListView.as_view(),name='departamento_list'),
    path('departamentos/crear/', DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamentos/editar/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('departamentos/eliminar/<int:pk>/', DepartamentoDeleteView.as_view(), name='departamento_delete'),

    # ------------------Inicio Del Model Cargo--------------------------------
    path('cargo', views.listar_cargos, name='listar_cargos'),
    path('cargos/crear/', CargoCreateView.as_view(), name='cargo_create'),
    path('cargos/editar/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/eliminar/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),

    # ------------------Inicio Del Model Departamento--------------------------------
    path('empleado', views.listar_empleados, name='listar_empleados'),
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
]
